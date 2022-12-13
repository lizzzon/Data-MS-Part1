from contextvars import ContextVar
from typing import Optional

from apps.config.database import DataBaseConfig
from apps.models.database_models import UserModel


connect = DataBaseConfig().connect()

current_user: ContextVar[Optional[UserModel]] = ContextVar('current_user', default=None)
current_client: ContextVar[Optional[UserModel]] = ContextVar('current_client', default=None)
current_company: ContextVar[Optional[UserModel]] = ContextVar('current_company', default=None)
current_staff: ContextVar[Optional[UserModel]] = ContextVar('current_staff', default=None)
