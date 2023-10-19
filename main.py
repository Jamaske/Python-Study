import sqlite3
db = sqlite3.connect('DataBase')
cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS table1 ')