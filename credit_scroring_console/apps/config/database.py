import psycopg2

class DataBaseConfig:

    _connection_conf = {
        "host": "localhost",
        "database": "credit_scoring",
        "user": "postgres",
        "password": "postgrespw",
        "port": "49153",
    }

    def connect(self):
        return psycopg2.connect(**self._connection_conf)
