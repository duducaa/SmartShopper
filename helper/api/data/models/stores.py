from base import Base
from peewee import *

class Stores(Base):
    name = TextField(db_column="store_name")
    logo = TextField(db_column="logo_path")