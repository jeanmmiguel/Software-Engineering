"""delete star2

Revision ID: 2259263142ff
Revises: 64fb59665d35
Create Date: 2022-05-30 17:20:15.436159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2259263142ff'
down_revision = '64fb59665d35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as  batch_op:
        batch_op.drop_column('stars2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('stars2', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
