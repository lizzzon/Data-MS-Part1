import os
from django.db import connection


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'credit_scoring.settings')

    with open('apps/orm/sql/migration.sql') as mf:
        sql_migration_script = mf.read()
        with connection.cursor() as cursor:
            cursor.execute(sql_migration_script)

    print('Success migrate')

if __name__ == '__main__':
    main()
