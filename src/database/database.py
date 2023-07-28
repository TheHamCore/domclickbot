from src.cfg.config import HOST, DATABASE, PORT, PASSWORD_DB, USER_DB, SCHEMA
import psycopg2


class Database:
    def __init__(self):
        self.connection_settings: str = self.connection()

    @staticmethod
    def connection() -> str:
        connection_settings: dict = {
            'host': HOST,
            'port': PORT,
            'dbname': DATABASE,
            'user': USER_DB,
            'password': PASSWORD_DB
        }
        connection_string = " ".join([f"{key}={value}" for key, value in connection_settings.items()])
        return connection_string

    def insert_to_database(self, query: str):
        with psycopg2.connect(self.connection_settings) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()

    def get_data_from_database(self,
                               query: str,
                               is_one_row: bool = False) -> list:
        with psycopg2.connect(self.connection_settings) as conn:
            # Создаем курсор для выполнения SQL-запросов
            with conn.cursor() as cursor:
                cursor.execute(query)
                if is_one_row:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
                return result
