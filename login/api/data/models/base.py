from peewee import MySQLDatabase, Model

db = MySQLDatabase(
    "smartshopper_db",
    user="smartshopper",
    host="172.168.200.5",
    port=3306,
    password="Password-1",
    charset='utf8mb4'
)

class Base(Model):
    class Meta:
        database = db