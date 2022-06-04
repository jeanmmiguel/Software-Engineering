"""empty message

Revision ID: 5da5b34643c6
Revises: 
Create Date: 2022-06-04 15:58:44.702420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5da5b34643c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id_evento', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('duration_time', sa.String(length=15), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_evento')
    )
    op.create_table('prefeitura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id_usuario')
    )
    op.drop_table('ORGANIZADOR')
    op.drop_table('USER')
    op.drop_table('LOCAL')
    op.drop_table('USUARIO_PARTICIPA_EVENTO')
    op.drop_table('PREFEITURA')
    op.drop_table('EVENT')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('EVENT',
    sa.Column('id_evento', sa.INTEGER(), nullable=True),
    sa.Column('duration_time', sa.NUMERIC(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('status', sa.NUMERIC(), nullable=True),
    sa.Column('price', sa.NUMERIC(), nullable=True),
    sa.PrimaryKeyConstraint('id_evento')
    )
    op.create_table('PREFEITURA',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('USUARIO_PARTICIPA_EVENTO',
    sa.Column('id_usuario', sa.INTEGER(), nullable=True),
    sa.Column('id_evento', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id_evento', 'id_usuario')
    )
    op.create_table('LOCAL',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('nome', sa.TEXT(), nullable=True),
    sa.Column('descricao', sa.TEXT(), nullable=True),
    sa.Column('qtde_maxima', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('USER',
    sa.Column('id_usuario', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id_usuario')
    )
    op.create_table('ORGANIZADOR',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('nome', sa.TEXT(), nullable=True),
    sa.Column('responsavel', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    op.drop_table('prefeitura')
    op.drop_table('event')
    # ### end Alembic commands ###
