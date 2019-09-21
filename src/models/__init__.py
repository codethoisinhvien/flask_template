from peewee import *
from src.models.user import User
from src.models.file import File
from config.database_config import database_name, host, port, password, user_name
db = MySQLDatabase(database_name, user=user_name, password=password, charset='utf8mb4', host=host, port=port)

def create_database():
    db.create_tables([User,File],safe=True)