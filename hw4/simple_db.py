import sqlite3

DATABASE_NAME = "census.db"


def read_density(con, table):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    for i in cur.fetchall():
        print(i[0], i[1] / i[2])
    print("")


def read_land_less(con, table, less):
    cur = con.cursor()
    cur.execute(f"SELECT province_or_teritory FROM {table} WHERE land_area < {less}")
    for i in cur.fetchall():
        print(i[0])
    print("")


def read_less_more(con, table, less, more):
    cur = con.cursor()
    cur.execute(f"SELECT province_or_teritory FROM {table} WHERE population < {less} OR population > {more}")
    for i in cur.fetchall():
        print(i[0])
    print("")


def read_less_mill(con, table, less):
    cur = con.cursor()
    cur.execute(f"SELECT province_or_teritory FROM {table} WHERE population < {less}")
    for i in cur.fetchall():
        print(i[0])
    print("")


def read_population(con, table):
    cur = con.cursor()
    cur.execute(f"SELECT population FROM {table}")
    for i in cur.fetchall():
        print(i[0])
    print("")


def read_database(con, table):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    for i in cur.fetchall():
        print(i)
    print("")


def fill_database(con, data):
    cur = con.cursor()
    for i in data:
        cur.execute(f"INSERT INTO density VALUES ('{i[0]}', {i[1]}, {i[2]})")


def create_database(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS density(province_or_teritory TEXT, population INTEGER, land_area REAL)")
    data = []
    with open("dataset1.csv", "r") as f:
        for line in f.readlines():
            line = line.strip().split(",")
            data.append(line)
    return data


if __name__ == '__main__':
    db = 'density'
    con = sqlite3.connect(DATABASE_NAME)
    data = create_database(con)
    fill_database(con, data)
    print("Everything:")
    read_database(con, db)
    print("Population:")
    read_population(con, db)
    print("Population less than 1M:")
    read_less_mill(con, db, 1000000)
    print("Population less than 1M or more than 5M:")
    read_less_more(con, db, 1000000, 5000000)
    print("Land Area more than 200K:")
    read_land_less(con, db, 200000)
    print("Density:")
    read_density(con, db)
    con.close()
