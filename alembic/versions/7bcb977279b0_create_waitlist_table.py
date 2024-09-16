"""create waitlist table

Revision ID: 7bcb977279b0
Revises: c811e03e818d
Create Date: 2024-09-16 02:08:24.232436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bcb977279b0'
down_revision: Union[str, None] = 'c811e03e818d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE waitlist (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE
        )
    """)

def downgrade() -> None:
    op.execute("DROP TABLE waitlist")
