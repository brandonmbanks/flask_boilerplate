"""empty message

Revision ID: 517a05824aae
Revises: 3fcd842d0ad4
Create Date: 2016-11-28 21:56:59.819417

"""

# revision identifiers, used by Alembic.
revision = '517a05824aae'
down_revision = '3fcd842d0ad4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
