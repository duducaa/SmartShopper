from base import Base
from peewee import *

class Users(Base):
    id = IntegerField(primary_key=True, db_column="user_id")
    email = TextField()
    password = TextField(db_column="hash_password")
    
    class Meta:
        table_name = "app_users"