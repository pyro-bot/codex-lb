"""Converge the account-credit and SCIM/overflow migration heads."""

revision = "20261003_000000_merge_account_credit_and_scim_overflow_heads"
down_revision = (
    "20260918_000000_merge_scim_and_overflow_heads",
    "20260922_010000_add_account_credit_namespace_planning",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
