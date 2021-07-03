import random
import time

from flask import Flask, g

app = Flask(__name__)


@app.before_request
def handle_request_start():
    g.started = time.time()


@app.after_request
def handle_request_stop(response):
    now = time.time()
    print('Request processing took - ', now - g.started)
    return response


@app.route("/")
def handle_root():
    rand_time = random.randint(1, 10) / 10
    time.sleep(rand_time)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
