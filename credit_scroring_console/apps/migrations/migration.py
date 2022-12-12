import os
from typing import Optional

from apps.config.config import connect


class Migrations:

    _migration_file = 'apps/migrations/sql_files/migration.sql'
    _filling_file = 'apps/migrations/sql_files/filling.sql'
    _procedures_file = 'apps/migrations/sql_files/procedures.sql'
    _triggers_file = 'apps/migrations/sql_files/triggers.sql'

    _files = (
        _migration_file,
        _filling_file,
        _procedures_file,
        _triggers_file,
    )

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

        for file in self._files:
            self.execute(file)
        self._cursor.close()

        print('Migrations success!')

    def execute(self, path: str) -> None:
        self._cursor.execute(self._read_sql_file(path))
        print(f'Execute {path}')
        connect.commit()
