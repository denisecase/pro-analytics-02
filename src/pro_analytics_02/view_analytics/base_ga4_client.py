"""Query anonymous page-level metrics from Google Analytics 4."""

from datetime import date
from typing import TypedDict

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Filter,
    FilterExpression,
    Metric,
    RunReportRequest,
    RunReportResponse,
)


class PageMetrics(TypedDict):
    """Anonymous aggregate metrics for one page path."""

    unique_visitors: int
    page_views: int


def build_page_report_request(
    property_id: str,
    start_date: date,
    end_date: date,
    path_prefix: str,
) -> RunReportRequest:
    """Build a GA4 request for page metrics within one repository path."""
    _validate_arguments(property_id, start_date, end_date, path_prefix)

    return RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[
            DateRange(
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat(),
            )
        ],
        dimensions=[Dimension(name="pagePath")],
        metrics=[
            Metric(name="totalUsers"),
            Metric(name="screenPageViews"),
        ],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="pagePath",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.BEGINS_WITH,
                    value=path_prefix,
                    case_sensitive=True,
                ),
            )
        ),
    )


def fetch_page_analytics(
    property_id: str,
    start_date: date,
    end_date: date,
    path_prefix: str,
    client: BetaAnalyticsDataClient | None = None,
) -> dict[str, PageMetrics]:
    """Run one GA4 report and return anonymous metrics keyed by page path."""
    request = build_page_report_request(
        property_id=property_id,
        start_date=start_date,
        end_date=end_date,
        path_prefix=path_prefix,
    )
    analytics_client = client or BetaAnalyticsDataClient()
    response = analytics_client.run_report(request=request)
    return parse_page_report_response(response)


def parse_page_report_response(
    response: RunReportResponse,
) -> dict[str, PageMetrics]:
    """Convert a GA4 response into JSON-compatible anonymous aggregates."""
    pages: dict[str, PageMetrics] = {}

    for row in response.rows:
        if len(row.dimension_values) != 1 or len(row.metric_values) != 2:
            raise ValueError(
                "The GA4 response does not match the requested report shape."
            )

        page_path = row.dimension_values[0].value
        pages[page_path] = PageMetrics(
            unique_visitors=_parse_count(
                row.metric_values[0].value,
                metric_name="totalUsers",
            ),
            page_views=_parse_count(
                row.metric_values[1].value,
                metric_name="screenPageViews",
            ),
        )

    return dict(sorted(pages.items()))


def _validate_arguments(
    property_id: str,
    start_date: date,
    end_date: date,
    path_prefix: str,
) -> None:
    if not property_id.isdecimal():
        raise ValueError("property_id must be the numeric GA4 property ID.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")
    if not path_prefix.startswith("/") or not path_prefix.endswith("/"):
        raise ValueError("path_prefix must start and end with '/'.")


def _parse_count(value: str, metric_name: str) -> int:
    try:
        count = int(value)
    except ValueError as error:
        message = f"GA4 returned a non-integer {metric_name}: {value!r}."
        raise ValueError(message) from error

    if count < 0:
        raise ValueError(f"GA4 returned a negative {metric_name}: {value!r}.")
    return count
