"""add user table

Revision ID: f8f274872b78
Revises: 387e7d336222
Create Date: 2024-11-20 23:48:38.219400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8f274872b78'
down_revision: Union[str, None] = '387e7d336222'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id', sa.Integer(),nullable =False),
                    sa.Column('email',sa.String(),nullable= False),
                    sa.Column('password',sa.String(),nullable= False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable= False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
