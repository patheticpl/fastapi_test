`"""empty message

Revision ID: c3efe38e216c
Revises: 
Create Date: 2024-01-23 23:52:48.539452

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3efe38e216c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Token_access_token'), 'Token', ['access_token'], unique=True)
    op.create_index(op.f('ix_Token_id'), 'Token', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Token_id'), table_name='Token')
    op.drop_index(op.f('ix_Token_access_token'), table_name='Token')
    op.drop_table('Token')
    op.drop_table('User')
    # ### end Alembic commands ###