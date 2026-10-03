## ADDED Requirements

### Requirement: Scoped account-credit usage

An API key MAY opt into the `account_credits` usage section. When enabled, `/v1/usage` SHALL return each accessible OpenAI account's known quota windows in codex-lb credits. A scoped key SHALL only receive its assigned accounts; an unscoped key SHALL receive all accessible accounts.

#### Scenario: One-to-one OpenAI credit mapping

- **WHEN** an account has a quota capacity of 100 credits and a stored used percentage of 25
- **THEN** its account-credit record reports 25 used credits and 75 remaining credits

### Requirement: Namespace planning is opt-in per API key

An API key MAY enable namespace planning. The default SHALL be disabled so existing model IDs and selection behavior remain unchanged.

