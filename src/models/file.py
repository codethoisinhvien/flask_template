from  peewee import *
from src.models.base_model import BaseModel
class File(BaseModel):
    name = TextField(unique=True)
    link = TextField(unique=True)

