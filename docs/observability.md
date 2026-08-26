# Observability

## Structured logging

Every request is logged as a single-line JSON object through custom middleware. Each entry includes a timestamp, log level, request ID, HTTP method, path, status code, and duration. JSON output allows logs to be parsed and queried by tools such as Grafana Loki, Datadog, or `jq`, rather than requiring manual review of plain text.

## Metrics

`GET /metrics` exposes metrics in Prometheus text format. No API key is required, since automated Prometheus scrapers must be able to reach this endpoint without credentials. In production deployments, this endpoint should instead be restricted at the network level (firewall rules or internal-only routing).

The endpoint tracks:

- `http_requests_total`: a counter labeled by method, path, and status code.
- `http_request_duration_seconds`: a histogram, enabling percentile-based queries (for example, p95 latency) rather than a single average value.

```bash
curl http://localhost:8000/metrics
```

### Planned improvements

- A Grafana dashboard reading from this endpoint.
- Alerting rules based on error rate or latency thresholds.

## Usage history

Every request is also persisted to a local SQLite database (`usage.db`) by the same middleware, recording method, path, status code, and duration. The database schema is created automatically on application startup; no manual setup step is required.

```bash
curl -H "X-API-Key: your-key-here" http://localhost:8000/usage  # gitleaks:allow
```

This endpoint returns the most recent requests (default 50, adjustable with the `limit` query parameter), ordered newest first. Because the logging middleware runs regardless of request outcome, rejected and unauthenticated requests are included, providing a complete audit trail rather than a log of successful calls only.

### Planned improvements

- Pagination beyond a flat limit.
- Filtering by path or status code.
- Migration to PostgreSQL if concurrent writes from multiple application instances become necessary; SQLite's single-file design does not handle concurrent writes from separate processes well.
