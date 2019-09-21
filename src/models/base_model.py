from peewee import *

from config.database_config import database_name, host, port, password, user_name

db = MySQLDatabase(database_name, user=user_name, password=password, charset='utf8mb4', host=host, port=port)


class BaseModel(Model):
    class Meta:
        database = db



