import requests
import json


def get_ip():
    URL = 'https://httpbin.org/ip'
    response = requests.get('https://httpbin.org/ip')
    if response.status_code >= 200:

        with open('my-ip.txt', 'w') as f:
            f.write(response.json()['origin'])


def count_word():
    URL = 'https://www.mes.gov.ge/index.php?lang=geo'
    response = requests.get(URL)
    if response.status_code >= 200:
        with open('ganatleba.txt', 'w') as f:
            cnt = response.text.count('განათლება')
            print(cnt)
            f.write(str(cnt))


if __name__ == '__main__':
    count_word()
    get_ip()