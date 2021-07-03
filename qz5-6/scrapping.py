import requests
import json
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = 'https://www.mes.gov.ge/content.php?id=6&lang=geo'
    response = requests.get(URL)
    html_tree = BeautifulSoup(response.text, "html.parser")
    info = html_tree.find("div", attrs={"class": "contactinfo"})
    all_info = info.find_all("span")
    address = all_info[0].text
    hot_line = all_info[1].text
    mail = all_info[3].text

    text_json = {
        "address": address,
        "hotline": hot_line,
        "mail": mail
    }
    to_file = json.dumps(text_json)

    with open("info.json", "w") as f:
        json.dump(to_file, f)
