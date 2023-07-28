import os
TOKEN: str = os.environ['TOKEN']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
DATABASE = os.environ['DATABASE']
USER_DB = os.environ['USER_DB']
PASSWORD_DB = os.environ['PASSWORD_DB']

MIN_CREDIT = float(os.environ['MIN_CREDIT'])
MAX_CREDIT = float(os.environ['MAX_CREDIT'])
SCHEMA = os.environ['SCHEMA']
