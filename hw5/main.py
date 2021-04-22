import sqlite3


def create_base(cur):
    cur.execute("DROP TABLE dataset")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS dataset "
        "(order_date DATE NOT NULL,"
        " region TEXT NOT NULL, "
        "client TEXT NOT NULL,"
        "item TEXT NOT NULL,"
        "units TEXT NOT NULL, "
        "unitcost TEXT NOT NULL, "
        "total TEXT NOT NULL)"
    )


def fillup_base(cur, con):
    with open("dataset2.csv", "r") as f:
        for line in f.readlines()[1:]:
            i = line.strip().split(",")
            cur.execute(
                "INSERT INTO dataset VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i[0], i[1], i[2], i[3],
                                                                                               i[4], i[5], i[6]))
    con.commit()


def read_base(cur):
    cur.execute("SELECT * FROM dataset")
    for i in cur.fetchall():
        print(i)


def read_cases(cur):
    cur.execute("SELECT total FROM dataset")
    print(list(map(lambda x: x[0], cur.fetchall())), "\n")

    cur.execute("SELECT client FROM dataset ORDER BY total DESC")
    print("Client who sold the most: ", cur.fetchone()[0])

    cur.execute("SELECT item FROM dataset ORDER BY units DESC")
    print("Most sold item: ", cur.fetchone()[0])

    cur.execute("SELECT SUM(unitcost) / COUNT(unitcost) FROM dataset")
    print("Average Price: ", cur.fetchone()[0])

    cur.execute("SELECT SUM(total) FROM dataset")
    print("Total Cost of products: ", cur.fetchone()[0])


if __name__ == '__main__':
    DATABASE = "base.db"
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    create_base(cur)
    fillup_base(cur, con)
    read_base(cur)
    read_cases(cur)
