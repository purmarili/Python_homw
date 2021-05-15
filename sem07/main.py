import json
from pprint import pprint

FILE_NAME = "test.json"

with open(FILE_NAME, "r") as fp:
    result = json.load(fp)

print(type(result))
# print(result)
res = result.get("users")
print(type(res), res)
