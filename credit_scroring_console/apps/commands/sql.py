from typing import Optional
from pydantic import BaseModel
import pymssql
import pandas as pd

from apps.config.config import connect
from apps.models.database_models import UserModel


class SQLCommands:

    @classmethod
    def _get_keys_values(cls, current_dict) -> tuple:
        keys, values = zip(*current_dict.items())
        keys = str(keys).replace("'", "")
        return keys, values

    @classmethod
    def get_user(cls, username: str) -> Optional[UserModel]:
        cursor = connect.cursor()
        cursor.execute(f"SELECT get_user('{username}')")
        result: tuple = cursor.fetchone()

        cursor.close()
        connect.commit()

        try:
            result = result[0].strip('()').split(',')
            result = [int(result[0])] + result[1:]  # type: ignore
        except Exception:
            return None

        return UserModel(**{k: v for k, v in zip(UserModel().dict().keys(), result)}) if result else None

    @classmethod
    def create_user(cls, user_dict: dict) -> None:
        cursor = connect.cursor()
        _, values = zip(*user_dict.items())
        cursor.execute(f'CALL insert_user{values}')

        cursor.close()
        connect.commit()

    @classmethod
    def update_user_active(cls, user_id: int, is_active: bool) -> None:
        cursor = connect.cursor()
        cursor.execute(f'CALL change_user_active({user_id}, {is_active})')

        cursor.close()
        connect.commit()

    @classmethod
    def select_one_execute(cls, table: str, where_str: str, model: BaseModel()) -> Optional[BaseModel]:
        cursor = connect.cursor()
        cursor.execute(f'SELECT * FROM {table} WHERE {where_str};')
        result: tuple = cursor.fetchone()

        cursor.close()
        connect.commit()

        return model(**{k: v for k, v in zip(model().dict().keys(), result)}) if result else None

    @classmethod
    def insert_execute(cls, table: str, dict_model: dict) -> None:
        cursor = connect.cursor()

        keys, values = cls._get_keys_values(dict_model)

        cursor.execute(f'INSERT INTO {table} {keys} VALUES {values};')

        cursor.close()
        connect.commit()

    @classmethod
    def delete_execute(cls, table: str, where_str: str) -> None:
        cursor = connect.cursor()

        cursor.execute(f'DELETE FROM {table} WHERE {where_str};')

        cursor.close()
        connect.commit()

    @classmethod
    def update_execute(cls, table: str, set_dict: dict, where_str: str) -> None:
        cursor = connect.cursor()

        set_dict = ','.join([f"{k}='{v}'" for k, v in set_dict.items()])
        cursor.execute(f'UPDATE {table} SET {set_dict} WHERE {where_str};')

        cursor.close()
        connect.commit()

    @classmethod
    def custom_execute(cls, query: str) -> None:
        cursor = connect.cursor()

        cursor.execute(query)

        cursor.close()
        connect.commit()

    @classmethod
    def custom_select_execute(cls, query: str) -> list:
        cursor = connect.cursor()

        cursor.execute(query)
        result: list = cursor.fetchall()

        cursor.close()
        connect.commit()

        return result
