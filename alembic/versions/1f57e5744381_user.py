"""user

Revision ID: 1f57e5744381
Revises: 4ffab0585781
Create Date: 2023-08-15 20:52:03.370070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f57e5744381'
down_revision: Union[str, None] = '4ffab0585781'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
