import json
from pprint import pprint

FILE_NAME = "result.json"
d = {
    "t": [1, 2, 3, 4],
    "b": (1, 2, 3),
    "JJJ": "test name"
}

with open(FILE_NAME, "w") as fp:
    json.dump(d, fp, indent=4)
