"""First migration

Revision ID: af738d1b1f65
Revises: b26f57973f92
Create Date: 2023-01-26 01:33:24.725969

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af738d1b1f65'
down_revision = 'b26f57973f92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sequence_number', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('final_message', sa.String(length=255), nullable=False),
    sa.Column('tasks', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('status', sa.Enum('preparing', 'started', 'finished', 'cancelled', name='statusshift'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('shift', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_shift_final_message'), ['final_message'], unique=False)

    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('ulr', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Enum('new', 'wait_report', 'under_review', 'approved', 'declined', name='statususertask'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('volunteer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('radius', sa.Text(), nullable=False),
    sa.Column('car', sa.Text(), nullable=False),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=13), nullable=False),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('volunteer_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'verified', 'declined', name='statususer'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_city'), ['city'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_phone_number'), ['phone_number'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_surname'), ['surname'], unique=False)

    op.create_table('assistance_disabled',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.Text(), nullable=False),
    sa.Column('street', sa.Text(), nullable=False),
    sa.Column('house', sa.Text(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('volunteer_id', sa.Integer(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('shift_id', sa.Integer(), nullable=True),
    sa.Column('numbers_lombaryers', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('active', 'excluded', name='statusmember'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['shift_id'], ['shift.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pollution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Text(), nullable=False),
    sa.Column('longitude', sa.Text(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('volunteer_id', sa.Integer(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('shift_id', sa.Integer(), nullable=True),
    sa.Column('attempt_number', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('active', 'excluded', name='statusmember'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['shift_id'], ['shift.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('shift_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('task_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('report_url', sa.String(length=255), nullable=True),
    sa.Column('uploaded_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('attempt_number', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('waiting', 'reviewing', 'approved', 'declined', name='statusreport'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['shift_id'], ['shift.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report')
    op.drop_table('request')
    op.drop_table('pollution')
    op.drop_table('member')
    op.drop_table('assistance_disabled')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_surname'))
        batch_op.drop_index(batch_op.f('ix_user_phone_number'))
        batch_op.drop_index(batch_op.f('ix_user_name'))
        batch_op.drop_index(batch_op.f('ix_user_city'))

    op.drop_table('user')
    op.drop_table('volunteer')
    op.drop_table('task')
    with op.batch_alter_table('shift', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_shift_final_message'))

    op.drop_table('shift')
    # ### end Alembic commands ###
