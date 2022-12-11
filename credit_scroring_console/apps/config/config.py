from contextvars import ContextVar
from typing import Optional

from apps.config.database import DataBaseConfig
from apps.models.database_models import UserModel


connect = DataBaseConfig().connect()

current_user: ContextVar[Optional[UserModel]] = ContextVar('current_user', default=None)
