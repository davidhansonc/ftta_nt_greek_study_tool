"""empty message

Revision ID: 02a6c2921660
Revises: 
Create Date: 2021-02-26 12:01:11.171473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02a6c2921660'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('new_testament',
    sa.Column('book', sa.String(), nullable=False),
    sa.Column('chapter', sa.Integer(), nullable=False),
    sa.Column('verse', sa.Integer(), nullable=False),
    sa.Column('recovery_version', sa.String(), nullable=True),
    sa.Column('nestle1904', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('book', 'chapter', 'verse')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_testament')
    # ### end Alembic commands ###
