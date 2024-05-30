import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user ( fullname TEXT NOT NULL , username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL , email TEXT NOT NULL , amount INTEGER NOT NULL);')




