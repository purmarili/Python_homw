import sqlite3

connection = sqlite3.connect('population.db')

cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pop_by_region(
    region TEXT NOT NULL,
    population INTEGER NOT NULL,
    PRIMARY KEY (region))''')

cursor.execute("INSERT INTO pop_by_region VALUES('Central Africa', 330993)")
cursor.execute("INSERT INTO pop_by_region VALUES('Southeastern Africa', 743112)")
cursor.execute("INSERT INTO pop_by_region VALUES('Japan', 100562)")
cursor.execute("INSERT INTO pop_by_region VALUES('Central Africa', 33099)")

print(cursor.execute("SELECT * from main.pop_by_region").fetchall())

connection.commit()
cursor.execute("DROP TABLE main.pop_by_region")
connection.commit()
connection.close()
