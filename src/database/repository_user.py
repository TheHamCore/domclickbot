from src.database.database import Database
from datetime import datetime

from src.database.query.query_user import get_sql_query_for_register, get_sql_query_for_check_user


class RepositoryUser(Database):
    def is_user_exist(self,
                      telegram_chat_id: int):
        query: str = get_sql_query_for_check_user(telegram_chat_id=telegram_chat_id)
        return self.get_data_from_database(query=query,
                                           is_one_row=True)

    def register_user(self,
                      first_name: str,
                      telegram_chat_id: int,
                      date: datetime.date):
        query: str = get_sql_query_for_register(first_name=first_name,
                                                telegram_chat_id=telegram_chat_id,
                                                date=date)
        self.insert_to_database(query=query)
