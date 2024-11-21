from base import Base
from peewee import *

class Products(Base):
    id = IntegerField(primary_key=True, db_column="product_id")
    name = TextField(db_column="product_name")
    target_price = DoubleField()
    user = ForeignKeyField()
    
    class Meta:
        table_name = "users_products"