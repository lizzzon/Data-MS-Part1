from typing import Optional

from apps.models.database_models import UserModel
from apps.config.config import connect

class UserCommands:

    @classmethod
    def select_user(cls, username) -> Optional[UserModel]:
        cursor = connect.cursor()

        cursor.execute(f"SELECT * FROM users WHERE username = '{username}';")
        result: tuple = cursor.fetchone()

        cursor.close()
        connect.commit()

        return UserModel(**{k: v for k, v in zip(UserModel().dict().keys(), result)}) if result else None

    @classmethod
    def insert_user(cls):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass
