"""empty message

Revision ID: 489c265ef67d
Revises: 545df6cabaf6
Create Date: 2020-01-02 13:03:04.125037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489c265ef67d'
down_revision = '545df6cabaf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'user', ['user_id'], ['id'])
    op.drop_column('task', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('user', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'user', ['user'], ['id'])
    # ### end Alembic commands ###