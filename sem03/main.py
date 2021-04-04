import sqlite3

# DATA grip
connection = sqlite3.connect("group_14.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS pop_by_region(region TEXT, population INTEGER)")

# cursor.execute("INSERT INTO pop_by_region VALUES ('TEST 1', 300987)")
# cursor.execute("INSERT INTO pop_by_region VALUES ('TEST 2', 3007)")
# cursor.execute("INSERT INTO pop_by_region VALUES ('TEST 44', 30093387)")
# cursor.execute("INSERT INTO pop_by_region VALUES ('TEST 12', 3987)")
#
# connection.commit()

cursor.execute("SELECT * FROM pop_by_region order by population desc")

max_row = cursor.fetchone()
print("Max:", max_row)

# for row in cursor.fetchall():
#     print(row)

if __name__ == '__main__':
    print("Finished")
