## 1. Backend

- [x] 1.1 Add persisted account routing names, API-key namespace-planning configuration, service-model configuration, and last successful account cursor with a forward-only migration and historical-row compatibility.
- [x] 1.2 Extend account and API-key admin APIs and schemas; invalidate account selection caches after routing-name changes.
- [x] 1.3 Add the opt-in scoped `account_credits` `/v1/usage` response section from stored usage telemetry.
- [x] 1.4 Normalize namespace requests, select pinned accounts, apply service-model cursor behaviour, and record successful routes.
- [x] 1.5 Emit scoped namespace entries in both model catalogues.

## 2. Frontend

- [x] 2.1 Add account routing-name and service-model administration controls.
- [x] 2.2 Add API-key usage-section and namespace-planning controls.

## 3. Verification

- [x] 3.1 Add usage, route-selection, catalogue and admin API tests.
- [ ] 3.2 Run backend lint/type/relevant integration tests and frontend lint/type/tests.
