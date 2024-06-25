from sqlalchemy import Column, Integer, VARCHAR, JSON, INTEGER
from core_lib.data_layers.data.db.sqlalchemy.base import Base
from core_lib.data_layers.data.db.sqlalchemy.mixins.soft_delete_mixin import SoftDeleteMixin

from notification_core_lib.constants import DEFAULT_PROJECT_ID


class Notification(Base, SoftDeleteMixin):

    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(VARCHAR(length=255), nullable=False)
    meta_data = Column(JSON())
    project_id = Column(INTEGER, nullable=False)
