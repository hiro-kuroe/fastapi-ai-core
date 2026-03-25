"""add cost and response time to ai usage logs

Revision ID: d138f4f79c82
Revises: d7c7fc802714
Create Date: 2026-03-24 22:13:27.986097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd138f4f79c82'
down_revision: Union[str, Sequence[str], None] = 'd7c7fc802714'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('ai_usage_logs', sa.Column('estimated_cost', sa.Float(), nullable=True))
    op.add_column('ai_usage_logs', sa.Column('response_time_ms', sa.Integer(), nullable=True))
    op.add_column('ai_usage_logs', sa.Column('endpoint', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('ai_usage_logs', 'endpoint')
    op.drop_column('ai_usage_logs', 'response_time_ms')
    op.drop_column('ai_usage_logs', 'estimated_cost')

