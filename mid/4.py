import json


def create_main_json():
    with open('data.json', 'r') as f:
        js = json.load(f)
        res = js['stats']
        with open('res.json', 'w') as wr:
            json.dump(res, wr, indent=4)


def create_json():
    js = json.dumps({'bla': 1, 'bu': 2, 'asd': ['he', 'hi']})
    res = {'asd': 'test', 'stats': js}
    with open('data.json', 'w') as f:
        json.dump(res, f, indent=4)


def read_json():
    with open('res.json', 'r') as f:
        print(json.load(f))


if __name__ == '__main__':
    create_json()
    create_main_json()
    read_json()
