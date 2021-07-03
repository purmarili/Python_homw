from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder="template")


@app.route('/')
def main():
    return 'Hello World!'


@app.route('/hello/<user>')
def hello(user):
    return f'Hello {user}'


if __name__ == '__main__':
    app.run(debug=True, port=5555, host='0.0.0.0')
