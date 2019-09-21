from  peewee import *
from src.models.base_model import BaseModel
class User(BaseModel):
    username = TextField()
    password = TextField()
    def get_user_by_username(self,username):

        query =self.select().where(username=username)
        return query.execute();
class Token (BaseModel):
    token = TextField();

