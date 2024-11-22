from base import Base
from peewee import *

class History(Base):
    id = IntegerField(primary_key=True, db_column="price_id")
    product_id = IntegerField()
    store_id = IntegerField()
    price = DoubleField()
    price_date = DateField()
    
    class Meta:
        table_name = "prices_history"