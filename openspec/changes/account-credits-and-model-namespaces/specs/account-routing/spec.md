## ADDED Requirements

### Requirement: Named OpenAI account routing

An administrator MAY assign a unique routing name to an OpenAI account. With namespace planning enabled, a request for `[routing_name] model` SHALL be routed only through that account and SHALL forward `model` upstream.

#### Scenario: Named model route

- **WHEN** `personal` is the routing name for an eligible OpenAI account
- **AND** an enabled key requests `[personal] gpt-6-sol`
- **THEN** the account is selected and `gpt-6-sol` is sent upstream

#### Scenario: Named account unavailable

- **WHEN** the named account is unavailable or inaccessible to the API key
- **THEN** the request fails without selecting a different named account

### Requirement: Administrator-managed service models

Administrators SHALL configure exact service-model names. Such models SHALL retain their original public name and use the API key's last successful eligible OpenAI account. With no OpenAI cursor, or after a non-OpenAI cursor, selection SHALL choose the eligible OpenAI account with greatest known remaining quota.

