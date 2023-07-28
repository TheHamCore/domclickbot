from datetime import datetime

from src.cfg.config import SCHEMA
from src.logger.logger_settings import logger


def get_sql_query_for_check_user(telegram_chat_id: int) -> str:
    query: str = f"""
    SELECT *
    FROM {SCHEMA}.user
    WHERE telegram_chat_id = {telegram_chat_id}
    """
    logger.debug(query)
    return query


def get_sql_query_for_register(first_name: str,
                               telegram_chat_id: int,
                               date: datetime.date) -> str:
    query: str = f"""
    INSERT INTO {SCHEMA}.user(first_name, telegram_chat_id, date)
                     VALUES('{first_name}', {telegram_chat_id}, '{date}')
    """
    logger.debug(query)
    return query
