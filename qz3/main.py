import sqlite3
import requests
from pprint import pprint


def create_base(con, cur):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employees (name TEXT NOT NULL, last_name TEXT, age INTEGER, city TEXT NOT NULL, salary REAL)")


def count_salary(con, cur):
    cur.execute("SELECT AVG(salary) FROM employees GROUP BY city")


if __name__ == '__main__':
    con = sqlite3.connect("persons.db")
    cur = con.cursor()
    create_base(con, cur)
    count_salary(con, cur)

    info = {
        "mark": "mercedes",
        "model": "A3",
        "factory": "Gocha",
        "price": 5000
    }

    MAPPING = {
        "text/html": "html",
        "image/png": "png",
        "image/jpeg": "jpg"
    }

    response = requests.get("https://httpbin.org/image/webp")
    print(response.headers["content-type"])
    with open("file.webp", "wb") as f:
        f.write(response.content)

    response = requests.post("https://httpbin.org/post", params=info)
    response_json = response.json()
    pprint(response_json)
