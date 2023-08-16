"""user

Revision ID: bf2535f7f60b
Revises: d5bfc1497fdf
Create Date: 2023-08-15 20:32:15.591132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf2535f7f60b'
down_revision: Union[str, None] = 'd5bfc1497fdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
