from base import Base
from peewee import *

from stores import Stores
from desired_products import Products

class Prices(Base):
    store = ForeignKeyField(Stores, backref="prices")
    product = ForeignKeyField(Products, backref="prices")
    price = FloatField()