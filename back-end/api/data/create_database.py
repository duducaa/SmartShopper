import sqlite3, os

db_path = os.getcwd() + "/data/db.sqlite3"

os.remove(db_path)
conn = sqlite3.connect(db_path)

sql = open(os.getcwd() + "/data/sql.sql", "r").read()

c = conn.cursor()

c.executescript(sql)