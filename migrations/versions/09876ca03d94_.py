"""empty message

<<<<<<< HEAD:migrations/versions/09876ca03d94_.py
Revision ID: 09876ca03d94
Revises: 
Create Date: 2022-06-09 00:40:03.977541
=======
Revision ID: 873137662d37
Revises: 
Create Date: 2022-06-09 02:04:19.801681
>>>>>>> desarrollo:migrations/versions/873137662d37_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<< HEAD:migrations/versions/09876ca03d94_.py
revision = '09876ca03d94'
=======
revision = '873137662d37'
>>>>>>> desarrollo:migrations/versions/873137662d37_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imagenes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('detalle', sa.String(length=120), nullable=True),
    sa.Column('firebase_id', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('firebase_id')
    )
    op.create_table('token_blocked_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_index(op.f('ix_token_blocked_list_email'), 'token_blocked_list', ['email'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('apellido', sa.String(length=120), nullable=False),
    sa.Column('fecha_ing', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('falla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('modelo', sa.String(length=120), nullable=False),
    sa.Column('fecha_creacion', sa.String(length=10), nullable=False),
    sa.Column('fecha_cierre', sa.String(length=10), nullable=True),
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
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('informe_tecnico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.Date(), nullable=False),
    sa.Column('comentario_servicio', sa.String(length=250), nullable=False),
    sa.Column('recomendacion', sa.String(length=250), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('falla_id', sa.Integer(), nullable=True),
    sa.Column('importe', sa.Float(), nullable=True),
    sa.Column('estado', sa.String(length=40), nullable=False),
    sa.ForeignKeyConstraint(['falla_id'], ['falla.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('propuesta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('detalle', sa.String(length=120), nullable=False),
    sa.Column('costo_servicio', sa.String(length=80), nullable=False),
    sa.Column('estado', sa.String(length=120), nullable=False),
    sa.Column('id_falla', sa.Integer(), nullable=True),
    sa.Column('id_tecnico', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id_falla'], ['falla.id'], ),
    sa.ForeignKeyConstraint(['id_tecnico'], ['perfil_tecnico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calificacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calificacion', sa.String(length=50), nullable=False),
    sa.Column('comentario', sa.String(length=250), nullable=False),
    sa.Column('id_tecnico', sa.Integer(), nullable=True),
    sa.Column('propuesta_id', sa.Integer(), nullable=True),
    sa.Column('fecha_cierre', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['id_tecnico'], ['perfil_tecnico.id'], ),
    sa.ForeignKeyConstraint(['propuesta_id'], ['propuesta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calificacion')
    op.drop_table('propuesta')
    op.drop_table('informe_tecnico')
    op.drop_table('perfil_tecnico')
    op.drop_table('falla')
    op.drop_table('user')
    op.drop_index(op.f('ix_token_blocked_list_email'), table_name='token_blocked_list')
    op.drop_table('token_blocked_list')
    op.drop_table('imagenes')
    # ### end Alembic commands ###
