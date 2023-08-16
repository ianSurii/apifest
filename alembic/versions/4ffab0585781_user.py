"""user

Revision ID: 4ffab0585781
Revises: bf2535f7f60b
Create Date: 2023-08-15 20:35:29.712661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ffab0585781'
down_revision: Union[str, None] = 'bf2535f7f60b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
