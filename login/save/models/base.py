from peewee import SqliteDatabase, Model

db = SqliteDatabase("../db.sqlite3")

class Base(Model):
    class Meta:
        database = db