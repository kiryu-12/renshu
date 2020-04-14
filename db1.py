import sqlite3

conn = sqlite3.connect('todolist.db')
curs = conn.cursor()

curs.execute('SELECT * FROM tasks')
rows = curs.fetchall()

print(rows)
