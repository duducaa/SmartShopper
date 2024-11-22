from peewee import *
from base import BaseModel

class Products(BaseModel):
    id = IntegerField(db_column="product_id", primary_key=True)
    name = TextField(db_column="product_name")
    target_price = DoubleField()
    user_id = IntegerField()
    
    class Meta:
        table_name = "users_products"