# Suggested Datasets: Continuous Intelligence

Good datasets for continuous intelligence typically represent
**systems that produce observations repeatedly over time**.
These systems can be monitored, analyzed for anomalies,
and evaluated for changes in behavior.

These are only suggestions.

## Choosing a Dataset

Look for datasets that represent **a system whose behavior can change over time**.

Good datasets usually:

- record observations repeatedly over time
- contain measurable system behavior (requests, rides, temperature, etc.)
- include enough observations to detect patterns or changes

Avoid datasets where:

- there is no time dimension
- the dataset is too small to change much
- there is no variable signal that can influence a decision

## Time-Ordered Observations

Continuous intelligence works best when observations occur **in sequence over time**.

If possible, use data that includes timestamps or another way to determine order.

This allows us to:

- sort observations chronologically
- compute rolling averages
- monitor behavior over time
- detect anomalies or drift

Example structure:

```text
timestamp,requests,errors,latency
2026-03-01 10:00,120,2,360
2026-03-01 10:05,130,2,380
2026-03-01 10:10,140,3,410
```

Even when timestamps are not available, a dataset can still work
if observations occur in a meaningful sequence (for example,
daily measurements or ordered events).

## Index

These datasets work well for applying continuous intelligence techniques.
More information in the sections below.

| Dataset                            | System Type                  | Good For Modules |
| ---------------------------------- | ---------------------------- | ---------------- |
| NYC Taxi Trips                     | Urban transportation demand  | 3, 4, 5          |
| Website Traffic Logs               | Online platform usage        | 3, 4, 5, 6       |
| System Monitoring Metrics          | DevOps system performance    | 2, 3, 4, 5, 6    |
| Air Quality Monitoring             | Environmental sensors        | 3, 4, 5          |
| Power Grid Load                    | Energy infrastructure        | 4, 5, 6          |
| GitHub Activity                    | Software development systems | 3, 4, 6          |
| Public Transportation Ridership    | Transit operations           | 4, 5, 6          |
| Transit Ridership (Example File)   | Small teaching dataset       | 2, 4, 5          |
| Web Service Metrics (Example File) | Small teaching dataset       | 2, 3, 4, 5, 6    |

## 1. NYC Taxi Trip Data

Source:
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

This dataset records taxi rides occurring across New York City over time.

Example fields:

- pickup_datetime
- trip_distance
- fare_amount
- passenger_count

Possible signals:

- rides per hour
- average trip distance
- average fare

Questions to explore:

- When do ride volumes spike?
- Are there anomalous days with unusually high or low demand?
- Does demand drift across weeks or seasons?

Works well for modules:

- Module 3: Signal Design
- Module 4: Rolling Monitoring
- Module 5: Drift Detection

## 2. Website Traffic Logs

Example datasets:

- https://www.kaggle.com/datasets/szymonjanowski/internet-traffic-data

These datasets represent website visits and user activity over time.

Example fields:

- timestamp
- visits
- page_views
- bounce_rate

Possible signals:

- visits per minute
- average session length
- page views per visitor

Questions to explore:

- When do traffic spikes occur?
- Are there sudden drops in activity?
- Is traffic trending upward or downward?

Works well for modules:

- Module 3: Signal Design
- Module 4: Rolling Monitoring
- Module 5: Drift Detection
- Module 6: System Assessment

## 3. System Monitoring Metrics

Example systems:

Prometheus-style monitoring metrics

Example datasets:

- https://prometheus.io/docs/introduction/overview/

Example fields:

- cpu_usage
- memory_usage
- disk_io
- requests
- errors
- latency

Possible analyses:

- detect unusually high CPU usage
- monitor rolling averages of system load
- detect latency drift

Questions to explore:

- When does system load spike?
- Does latency increase over time?
- Are there patterns in system performance?

Works well for modules:

- Module 2: Anomaly Detection
- Module 3: Signal Design
- Module 4: Rolling Monitoring
- Module 5: Drift Detection
- Module 6: System Assessment

## 4. Air Quality Monitoring

Source:
https://www.epa.gov/outdoor-air-quality-data

Air quality sensors record environmental conditions across time.

Example fields:

- timestamp
- pm25
- ozone
- temperature
- wind_speed

Possible analyses:

- pollution spikes
- rolling air quality averages
- seasonal environmental changes

Questions to explore:

- Are pollution spikes occurring?
- Are pollution levels drifting over time?
- How do weather conditions affect air quality?

Works well for modules:

- Module 3: Signal Design
- Module 4: Rolling Monitoring
- Module 5: Drift Detection

## 5. Power Grid Load

Source:
https://www.eia.gov/opendata/

Electricity demand datasets record power consumption over time.

Example fields:

- timestamp
- demand_mw
- generation_mw
- temperature

Possible signals:

- demand change rate
- peak demand periods
- rolling demand averages

Questions to explore:

- When does electricity demand spike?
- Are there daily or weekly cycles?
- Is demand increasing over time?

Works well for modules:

- Module 4: Rolling Monitoring
- Module 5: Drift Detection
- Module 6: System Assessment

## 6. GitHub Activity Data

Source:
https://www.githubarchive.org/

GitHub activity datasets track development activity across repositories.

Example fields:

- repository
- commits
- issues_opened
- pull_requests
- timestamp

Possible signals:

- commits per day
- issue creation rate
- development activity level

Questions to explore:

- Are some repositories inactive?
- Are there spikes in development activity?
- Does project activity change over time?

Works well for modules:

- Module 3: Signal Design
- Module 4: Rolling Monitoring
- Module 6: System Assessment

## 7. Public Transportation Ridership

Example dataset:

Chicago Transit Authority ridership data

https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f

Example fields:

- station
- rides
- timestamp

Possible signals:

- rides per hour
- rolling ridership
- weekday vs weekend demand

Possible anomalies:

- holidays
- snowstorms
- major events

Questions to explore:

- Are ridership levels changing over time?
- Are there unusual spikes or drops?
- How does demand vary across days or weeks?

Works well for modules:

- Module 4: Rolling Monitoring
- Module 5: Drift Detection
- Module 6: System Assessment

## 8. Transit Ridership (Example File)

Small example dataset included in this guide:

[transit_ridership.csv](files/transit_ridership.csv)

This dataset represents daily ridership observations and includes a spike that can represent a special event.

Possible analyses:

- detect anomalous ridership spikes
- compute rolling ridership averages
- observe gradual demand drift

Works well for modules:

- Module 2: Anomaly Detection
- Module 4: Rolling Monitoring
- Module 5: Drift Detection
- Module 6: System Assessment

## 9. Web Service Metrics (Example File)

Small example dataset included in this guide:

[web-service-metrics.csv](files/web-service-metrics.csv)

This dataset represents a web service under increasing load.

Example fields:

- requests
- errors
- total_latency_ms

Possible signals:

- error_rate = errors / requests
- avg_latency = total_latency_ms / requests

Possible analyses:

- detect error spikes
- monitor rolling latency trends
- detect performance drift under load

Works well for modules:

- Module 2: Anomaly Detection
- Module 3: Signal Design
- Module 4: Rolling Monitoring
- Module 5: Drift Detection
- Module 6: System Assessment
