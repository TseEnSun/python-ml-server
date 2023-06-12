"""Added tables

Revision ID: daa63eb9744a
Revises: 
Create Date: 2023-06-12 05:39:12.570292

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'daa63eb9744a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('target_search_uuid', sa.String(), nullable=True),
    sa.Column('target_search_term', sa.String(), nullable=True),
    sa.Column('target_search_result', sa.String(), nullable=False),
    sa.Column('feed_back_user', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feedback_feed_back_user'), 'feedback', ['feed_back_user'], unique=False)
    op.create_index(op.f('ix_feedback_id'), 'feedback', ['id'], unique=False)
    op.create_index(op.f('ix_feedback_target_search_term'), 'feedback', ['target_search_term'], unique=False)
    op.create_index(op.f('ix_feedback_target_search_uuid'), 'feedback', ['target_search_uuid'], unique=False)
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_uuid', sa.String(), nullable=True),
    sa.Column('search_term', sa.String(), nullable=True),
    sa.Column('search_result', sa.String(), nullable=False),
    sa.Column('search_user', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_search_search_term'), 'search', ['search_term'], unique=False)
    op.create_index(op.f('ix_search_search_user'), 'search', ['search_user'], unique=False)
    op.create_index(op.f('ix_search_search_uuid'), 'search', ['search_uuid'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_search_search_uuid'), table_name='search')
    op.drop_index(op.f('ix_search_search_user'), table_name='search')
    op.drop_index(op.f('ix_search_search_term'), table_name='search')
    op.drop_table('search')
    op.drop_index(op.f('ix_feedback_target_search_uuid'), table_name='feedback')
    op.drop_index(op.f('ix_feedback_target_search_term'), table_name='feedback')
    op.drop_index(op.f('ix_feedback_id'), table_name='feedback')
    op.drop_index(op.f('ix_feedback_feed_back_user'), table_name='feedback')
    op.drop_table('feedback')
    # ### end Alembic commands ###
