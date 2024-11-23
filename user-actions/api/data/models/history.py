from peewee import *
from base import BaseModel

class History(BaseModel):
    id = IntegerField(db_column="price_id", primary_key=True)
    product_id = IntegerField()
    store_id = IntegerField()
    price = DoubleField()
    price_date = TextField()
    
    class Meta:
        table_name = "prices_history"
