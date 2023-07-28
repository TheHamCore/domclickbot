from loguru import logger
logger.add('debug.log', format="{time} {level} {message}", level="DEBUG", rotation='200 MB', compression="tar")