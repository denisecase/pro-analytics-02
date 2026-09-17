"""Tests for Google Analytics 4 page reporting."""

from datetime import date
from unittest.mock import MagicMock

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DimensionValue,
    Filter,
    MetricValue,
    Row,
    RunReportResponse,
)
import pytest

from pro_analytics_02.view_analytics.base_ga4_client import (
    build_page_report_request,
    fetch_page_analytics,
    parse_page_report_response,
)


def make_response() -> RunReportResponse:
    """Create a representative GA4 response without contacting Google."""
    return RunReportResponse(
        rows=[
            Row(
                dimension_values=[
                    DimensionValue(value="/pro-analytics-02/workflow-b/")
                ],
                metric_values=[MetricValue(value="12"), MetricValue(value="18")],
            ),
            Row(
                dimension_values=[
                    DimensionValue(value="/pro-analytics-02/workflow-a/")
                ],
                metric_values=[MetricValue(value="31"), MetricValue(value="47")],
            ),
        ]
    )


def test_build_page_report_request() -> None:
    request = build_page_report_request(
        property_id="123456789",
        start_date=date(2026, 8, 24),
        end_date=date(2026, 9, 15),
        path_prefix="/pro-analytics-02/",
    )

    assert request.property == "properties/123456789"
    assert request.date_ranges[0].start_date == "2026-08-24"
    assert request.date_ranges[0].end_date == "2026-09-15"
    assert [dimension.name for dimension in request.dimensions] == ["pagePath"]
    assert [metric.name for metric in request.metrics] == [
        "totalUsers",
        "screenPageViews",
    ]
    assert request.dimension_filter.filter.field_name == "pagePath"
    assert request.dimension_filter.filter.string_filter.match_type == (
        Filter.StringFilter.MatchType.BEGINS_WITH
    )
    assert request.dimension_filter.filter.string_filter.value == ("/pro-analytics-02/")
    assert request.dimension_filter.filter.string_filter.case_sensitive is True


def test_parse_page_report_response_returns_sorted_anonymous_metrics() -> None:
    pages = parse_page_report_response(make_response())

    assert pages == {
        "/pro-analytics-02/workflow-a/": {
            "unique_visitors": 31,
            "page_views": 47,
        },
        "/pro-analytics-02/workflow-b/": {
            "unique_visitors": 12,
            "page_views": 18,
        },
    }


def test_fetch_page_analytics_runs_one_report() -> None:
    client = MagicMock(spec=BetaAnalyticsDataClient)
    client.run_report.return_value = make_response()

    pages = fetch_page_analytics(
        property_id="123456789",
        start_date=date(2026, 8, 24),
        end_date=date(2026, 9, 15),
        path_prefix="/pro-analytics-02/",
        client=client,
    )

    client.run_report.assert_called_once()
    assert pages["/pro-analytics-02/workflow-a/"]["unique_visitors"] == 31
    assert pages["/pro-analytics-02/workflow-a/"]["page_views"] == 47


@pytest.mark.parametrize(
    ("property_id", "start_date", "end_date", "path_prefix", "message"),
    [
        (
            "G-ABC123",
            date(2026, 8, 24),
            date(2026, 9, 15),
            "/pro-analytics-02/",
            "numeric GA4 property ID",
        ),
        (
            "123456789",
            date(2026, 9, 16),
            date(2026, 9, 15),
            "/pro-analytics-02/",
            "start_date",
        ),
        (
            "123456789",
            date(2026, 8, 24),
            date(2026, 9, 15),
            "pro-analytics-02",
            "path_prefix",
        ),
    ],
)
def test_build_page_report_request_rejects_invalid_arguments(
    property_id: str,
    start_date: date,
    end_date: date,
    path_prefix: str,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        build_page_report_request(
            property_id=property_id,
            start_date=start_date,
            end_date=end_date,
            path_prefix=path_prefix,
        )


def test_parse_page_report_response_rejects_an_unexpected_shape() -> None:
    response = RunReportResponse(
        rows=[
            Row(
                dimension_values=[DimensionValue(value="/pro-analytics-02/")],
                metric_values=[MetricValue(value="31")],
            )
        ]
    )

    with pytest.raises(ValueError, match="report shape"):
        parse_page_report_response(response)
