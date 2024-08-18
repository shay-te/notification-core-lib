import enum
from datetime import datetime

from core_lib.data_layers.data.db.sqlalchemy.types.int_enum import IntEnum
from sqlalchemy import Column, Integer, VARCHAR, JSON, INTEGER, DateTime, ForeignKey, Index
from core_lib.data_layers.data.db.sqlalchemy.base import Base
from core_lib.data_layers.data.db.sqlalchemy.mixins.soft_delete_mixin import SoftDeleteMixin


class Notification(Base, SoftDeleteMixin):

    __tablename__ = 'notification'
    INDEX_TITLE_CREATED_AT = 'index_title_created_at'

    class NotificationType(enum.Enum):
        # Search event
        NEW_MATCH = 1  # <i class="fa-solid fa-heart"></i>
        NEW_RELATIONSHIP = 2

        # Relationship events
        PARTNER_PHOTO_EXPOSE = 10  # <i class="fa-solid fa-eye"></i>
        CONVERSATION_STARTED = 11
        CONVERSATION_ENDED = 12
        CONVERSATION_CODE_AGREED = 13
        DATE_SCHEDULED = 14
        CHAT_EXPOSED = 15
        ASK_CLARIFYING_QUESTION = 16
        RELATIONSHIP_PHOTO_EXPOSED = 16

        # Register events
        REGISTER_FINISHED = 100

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(VARCHAR(length=255), nullable=False)
    meta_data = Column(JSON())
    project_id = Column(INTEGER, nullable=False)


    Index(INDEX_TITLE_CREATED_AT, 'title', 'created_at', unique=True),

