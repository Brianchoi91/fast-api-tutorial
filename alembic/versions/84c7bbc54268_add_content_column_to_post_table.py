"""add content column to post table

Revision ID: 84c7bbc54268
Revises: bcf84cd75617
Create Date: 2022-04-11 14:03:52.940485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84c7bbc54268'
down_revision = 'bcf84cd75617'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
