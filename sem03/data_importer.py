"""
0. შევქმნათ ცხრილი მონაცემთა ბაზაში scv ფაილში არსებული ინფორმაციისთვის
1. წავიკითხოთ csv ფაილი და ჩავტვირთოთ მონაცემთა ბაზაში.
2. გამოვიყენოთ კლასი მონაცემების ტრანსფერისთვის
3. ვიპოვოთ ყველაზე მაღალანაზღაურებადი პერსონა
4. ვიპოვოთ ყველაზე მაღალანაზღაურებადი პერსონა კონკრეტულ ასაკის დიაპაზონში. მაგ: 20-40
"""
import sqlite3
DATA_FILE_NAME = "group_14.db"


def create_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employees(name TEXT, surname TEXT)")
    return cur


def load_data(f_name):
    result = []
    with open(f_name, "r") as f:
        for line in f.readlines():
            row = line.strip().split(",")
            print(row)
            break
    return result


def main():
    connection = sqlite3.connect(DATA_FILE_NAME)
    create_table(connection)
    data = load_data(DATA_FILE_NAME)

    connection.close()


if __name__ == '__main__':
    main()
