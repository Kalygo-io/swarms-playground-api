"""add reset token to account table

Revision ID: c811e03e818d
Revises: e593a644355a
Create Date: 2024-09-07 19:35:49.677698

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c811e03e818d'
down_revision: Union[str, None] = 'e593a644355a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TABLE accounts ADD COLUMN reset_token VARCHAR(64);")

def downgrade() -> None:
    pass
    # op.execute("ALTER TABLE accounts DROP COLUMN reset_token;")
