"""Add scoped account-credit and namespace-planning persistence.

Revision ID: 20260922_010000_add_account_credit_namespace_planning
Revises: 20260914_000000_add_scim_tokens, 20260914_000000_drop_subscription_overflow_schema
"""

import sqlalchemy as sa
from alembic import op

revision = "20260922_010000_add_account_credit_namespace_planning"
down_revision = ("20260914_000000_add_scim_tokens", "20260914_000000_drop_subscription_overflow_schema")
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("accounts") as batch_op:
        batch_op.add_column(sa.Column("routing_name", sa.String(length=64), nullable=True))
        batch_op.create_unique_constraint("uq_accounts_routing_name", ["routing_name"])
    with op.batch_alter_table("api_keys") as batch_op:
        batch_op.add_column(
            sa.Column("namespace_planning_enabled", sa.Boolean(), nullable=False, server_default=sa.false())
        )
    op.create_table(
        "api_key_route_cursors",
        sa.Column("api_key_id", sa.String(), nullable=False),
        sa.Column("account_id", sa.String(), nullable=True),
        sa.Column("is_openai_account", sa.Boolean(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["accounts.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["api_key_id"], ["api_keys.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("api_key_id"),
    )
    op.create_table(
        "service_models",
        sa.Column("model", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("model"),
    )


def downgrade() -> None:
    op.drop_table("service_models")
    op.drop_table("api_key_route_cursors")
    with op.batch_alter_table("api_keys") as batch_op:
        batch_op.drop_column("namespace_planning_enabled")
    with op.batch_alter_table("accounts") as batch_op:
        batch_op.drop_constraint("uq_accounts_routing_name", type_="unique")
        batch_op.drop_column("routing_name")
