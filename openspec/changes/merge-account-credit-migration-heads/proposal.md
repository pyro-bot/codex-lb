# Proposal

## Why

The merged repository has two Alembic heads, so database upgrades fail before the application can start. Production may already be stamped at the account-credit revision, while another branch introduced an empty merge revision.

## What Changes

- Add a forward-only Alembic merge revision above both existing heads.
- Preserve both existing revision IDs and their migration bodies.
- Verify upgrades from each existing head retain data and reach one canonical head.

## Capabilities

### Modified Capabilities

- `database-migrations`: require a data-preserving convergence path from either existing head.

## Impact

Alembic revision graph, database startup upgrades, and migration verification.
