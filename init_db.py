import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO simpsons (name, age) VALUES (?, ?)", ('Homer Simpson', 39))

cur.execute("INSERT INTO simpsons (name, age) VALUES (?, ?)", ('Marge Simpson', 36))

cur.execute("INSERT INTO simpsons (name, age) VALUES (?, ?)", ('Bart Simpson', 10))

connection.commit()
connection.close()
