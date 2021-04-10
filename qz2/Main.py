class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


def create_base():
    import sqlite3
    DATABASE_NAME = "morty.db"
    connection = sqlite3.connect(DATABASE_NAME)
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dogs (name TEXT, age INTEGER, color TEXT)")

    cur.execute("INSERT INTO dogs VALUES('CHAPA', 5, 'YAVISFERI')")
    cur.execute("INSERT INTO dogs VALUES('JEKA', 5, 'WITELI')")
    cur.execute("INSERT INTO dogs VALUES('TONY', 5, 'SHAVI')")

    cur.execute("SELECT * FROM dogs")
    print(cur.fetchall())


if __name__ == '__main__':
    f1 = Fruit("marwyvi", 5)
    f2 = Fruit("kenkra", 10)
    f3 = Fruit("marwyvi", 5)
    f = f1 + f2
    print(f)
    print(f1 == f2)
    print(f1 == f3)
    create_base()
