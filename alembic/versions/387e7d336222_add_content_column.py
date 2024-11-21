"""add content column

Revision ID: 387e7d336222
Revises: 06c316a0adb1
Create Date: 2024-11-20 23:45:21.600453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '387e7d336222'
down_revision: Union[str, None] = '06c316a0adb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
