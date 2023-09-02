"""primary models

Revision ID: 6fcd36ebfa50
Revises: 
Create Date: 2023-09-02 03:19:34.353200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fcd36ebfa50'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('m2m_users_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_m2m_users_groups_group_id'), 'm2m_users_groups', ['group_id'], unique=False)
    op.create_index(op.f('ix_m2m_users_groups_user_id'), 'm2m_users_groups', ['user_id'], unique=False)
    op.create_index('user_group_together', 'm2m_users_groups', ['user_id', 'group_id'], unique=False)
    op.create_table('audits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('INCLUDE', 'EXCLUDE', name='eventtype'), nullable=False),
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('m2m_user_group_id', sa.Integer(), nullable=False),
    sa.Column('dt', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['m2m_user_group_id'], ['m2m_users_groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('audits')
    op.drop_index('user_group_together', table_name='m2m_users_groups')
    op.drop_index(op.f('ix_m2m_users_groups_user_id'), table_name='m2m_users_groups')
    op.drop_index(op.f('ix_m2m_users_groups_group_id'), table_name='m2m_users_groups')
    op.drop_table('m2m_users_groups')
    op.drop_table('users')
    op.drop_table('groups')
    # ### end Alembic commands ###