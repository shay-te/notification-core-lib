"""create_db

Revision ID: 1
Revises: 
Create Date: 2024-04-08 13:02:44.387345

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

from notification_core_lib.data_layers.data.db.entities.notification import Notification
from notification_core_lib.data_layers.data.db.entities.user_notification import UserNotification

# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        Notification.__tablename__,
        sa.Column(Notification.id.key, sa.Integer, primary_key=True, nullable=False),
        sa.Column(Notification.title.key, sa.VARCHAR(length=255), nullable=False),
        sa.Column(Notification.meta_data.key, sa.JSON),
        sa.Column(Notification.project_id.key, sa.Integer, nullable=False),

        sa.Column(Notification.created_at.key, sa.DateTime, default=datetime.utcnow),
        sa.Column(Notification.updated_at.key, sa.DateTime, default=datetime.utcnow),
        sa.Column(Notification.deleted_at.key, sa.DateTime, default=None),
    )

    op.create_table(
        UserNotification.__tablename__,
        sa.Column(UserNotification.id.key, sa.Integer, primary_key=True, nullable=False),
        sa.Column(UserNotification.user_id.key, sa.Integer, nullable=False),
        sa.Column(UserNotification.read_at.key, sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table(UserNotification.__tablename__)
    op.drop_table(Notification.__tablename__)
