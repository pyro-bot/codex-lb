# Spec Delta

## ADDED Requirements

### Requirement: Account-credit migration heads converge without data changes
The migration graph MUST have one canonical head descending from both `20260918_000000_merge_scim_and_overflow_heads` and `20260922_010000_add_account_credit_namespace_planning`. Upgrading a database stamped at either revision MUST preserve existing rows and apply each schema-changing revision at most once. The convergence revision's upgrade and downgrade MUST NOT modify application schema or data.

#### Scenario: Production account-credit revision upgrades
- **WHEN** a database stamped at `20260922_010000_add_account_credit_namespace_planning` upgrades to head
- **THEN** it reaches the canonical head without recreating account-credit tables or changing existing account and API-key rows

#### Scenario: Other merged head upgrades
- **WHEN** a database stamped at `20260918_000000_merge_scim_and_overflow_heads` upgrades to head
- **THEN** the account-credit schema is applied once and existing rows remain intact
