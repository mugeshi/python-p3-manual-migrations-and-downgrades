"""Renaming students to scholars

Revision ID: f4f4bbc5cd38
Revises: 791279dd0760
Create Date: 2023-09-05 15:05:58.867415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4f4bbc5cd38'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
