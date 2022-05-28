"""empty message

Revision ID: 17c3c40522fc
Revises: 
Create Date: 2022-05-28 01:13:53.180785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17c3c40522fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('apellido', sa.String(length=120), nullable=False),
    sa.Column('fecha_ing', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('apellido'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('fecha_ing'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('falla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('modelo', sa.String(length=120), nullable=False),
    sa.Column('fecha_creacion', sa.Integer(), nullable=False),
    sa.Column('fecha_cierre', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=False),
    sa.Column('estado', sa.String(length=5), nullable=False),
    sa.Column('ubicacion', sa.String(length=200), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('perfil_tecnico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('historial', sa.String(length=120), nullable=False),
    sa.Column('ubicacion', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('historial'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('perfil_tecnico')
    op.drop_table('falla')
    op.drop_table('user')
    # ### end Alembic commands ###
