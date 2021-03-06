"""empty message

Revision ID: 750f5232e59d
Revises: 2199cfc2fba4
Create Date: 2021-08-03 20:40:42.985620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '750f5232e59d'
down_revision = '2199cfc2fba4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_subject',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('subject_id', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('subject_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_subject')
    # ### end Alembic commands ###
