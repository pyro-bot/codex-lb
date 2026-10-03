## Decisions

### Account credits are live account telemetry, not an API-key counter

`account_credits` reports upstream usage snapshots for each account accessible to the caller. The system computes a window's consumed credits as `capacity_credits * used_percent / 100`; it does not update `ApiKeyLimit(CREDITS)`. This is exact per account, but cannot attribute an upstream account's total to one API key if keys share the account.

### Namespaces pin, not fail over

`[personal] gpt-6-sol` resolves before normal source selection and may use only the OpenAI account whose unique `routing_name` is `personal`. The normalized upstream model is `gpt-6-sol`. An unavailable named account returns a clear route error rather than silently switching namespace.

### Service models are data

Administrators set the service-model names in the dashboard. Matching is exact and case-sensitive. A service model retains its original public model ID and is resolved through a durable successful-route cursor per API key. The cursor records only successful proxy routes. A remembered named OpenAI account is reused while it remains eligible; a non-OpenAI, unnamed, unavailable, or absent remembered route selects the eligible OpenAI account with the greatest remaining credit balance.
