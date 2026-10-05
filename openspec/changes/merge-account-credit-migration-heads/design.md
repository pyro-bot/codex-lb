# Design

## Context

The account-credit revision and the earlier empty SCIM/overflow merge revision have the same two parents. Both revisions are already in merged history, and production may be stamped at the account-credit revision.

## Goals / Non-Goals

**Goals:** Keep both historical revision IDs valid and converge on one head from either deployed state.

**Non-Goals:** Change account-credit schema or backfill data.

## Decisions

Add a new empty Alembic revision whose parents are both current heads. Repointing an existing revision would change published migration history; the new node lets Alembic traverse only the missing branch from either deployed state.

## Risks / Trade-offs

- A database already stamped with both heads must still converge. Verify the upgrade path on a disposable SQLite database.
- PostgreSQL-specific DDL in the account-credit revision is outside the empty merge itself. Preserve the original migration and verify graph topology plus available SQLite paths locally.

## Migration Plan

Deploy the build with the new revision and run the normal `upgrade head` process. From the account-credit head, Alembic records the empty sibling and merge revisions. From the earlier merge head, it runs the account-credit revision once. Rollback to either branch requires an explicit target revision, as with any Alembic merge node.
