from string import Template

from django.db import connections


class TemplateQuerySQL:
    SELECT_ALL = Template('SELECT * FROM $table;')
    SELECT_BY_VALUE = Template('SELECT * FROM $table WHERE $where_value;')
    INSERT = Template('INSERT INTO $table $i_keys VALUES $i_values;')
    UPDATE = Template('UPDATE $table SET $set_value WHERE $where_values;')
    DELETE = Template('DELETE FROM $table WHERE $where_values;')

    @classmethod
    def create_cursor(cls):
        return connections['default'].cursor()

    def select_all(self, table: str) -> str:
        return self.SELECT_ALL.substitute(table=table)

    def select(self, table: str, where_values: str) -> str:
        return self.SELECT_BY_VALUE.substitute(table=table, where_value=where_values)

    def insert(self, table: str, insert_value: dict) -> str:
        i_keys, i_values = zip(*insert_value.items())
        i_keys = str(i_keys).replace("'", "")
        return self.INSERT.substitute(table=table, i_keys=i_keys, i_values=i_values)

    def update(self, table: str, set_value: dict, where_values: str) -> str:
        set_value = ','.join([f'{k}={v}' for k, v in set_value.items()])
        return self.UPDATE.substitute(table=table, set_value=set_value, where_values=where_values)

    def delete(self, table: str, where_values: str) -> str:
        return self.UPDATE.substitute(table=table, where_values=where_values)
