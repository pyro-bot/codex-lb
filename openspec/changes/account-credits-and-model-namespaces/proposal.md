## Why

An API key can currently see a global aggregate of upstream quota, even when the key is restricted to a subset of accounts. It also cannot deliberately select an individual OpenAI account when several accounts expose the same model. Operators need scoped account-credit reporting and an opt-in way to expose intentionally separated account routes.

## What Changes

- Add the opt-in `account_credits` usage section. `/v1/usage` returns the accessible OpenAI accounts' stored quota windows in credits; one upstream OpenAI credit equals one codex-lb credit.
- Add administrator-managed account routing names and a per-key namespace-planning toggle. A request for `[name] model` is pinned to that named OpenAI account and forwards `model` upstream.
- Add administrator-managed service-model names. They are never namespaced. In planning mode, they use the API key's last successful named OpenAI account, or the eligible OpenAI account with the greatest remaining quota when no such route exists.
- Publish eligible virtual namespace models from both OpenAI and Codex model catalogues.

## Impact

- `app/db/models.py` and a new Alembic revision
- account, API-key, proxy-routing and model-catalog modules
- React account/API-key administration screens and translations
- usage, routing and catalogue regression tests

