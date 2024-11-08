from base import Base
from peewee import *

class Desired_Products(Base):
    name = TextField(db_column="product_name")
    target_price = FloatField()
    image = TextField(db_column="db_path")
    
    class Meta:
        db_table = "desired_products"