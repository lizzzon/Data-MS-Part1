import os
from typing import Optional

from apps.config.config import connect


class Migrations:

    _migration_file = 'apps/migrations/migration.sql'
    _procedures_file = 'apps/migrations/procedures.sql'
    _triggers_file = 'apps/migrations/triggers.sql'

    def __init__(self):
        self._cursor = connect.cursor()

    @classmethod
    def _read_sql_file(cls, path: str) -> Optional[str]:
        if not os.path.exists(path):
            print(f'File {path} does not exists!')
            return None

        with open(path, 'r') as rf:
            return rf.read()

    def make_migrate(self) -> None:
        print('Start migrations')

        self.migration()
        # self.procedures()
        # self.triggers()
        self._cursor.close()

        print('Migrations success!')

    def migration(self) -> None:
        self._cursor.execute(self._read_sql_file(self._migration_file))
        connect.commit()

    def procedures(self) -> None:
        self._cursor.execute(self._read_sql_file(self._procedures_file))
        connect.commit()

    def triggers(self) -> None:
        self._cursor.execute(self._read_sql_file(self._triggers_file))
        connect.commit()
