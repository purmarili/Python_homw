import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

if __name__ == '__main__':
    URL = 'https://quotes.toscrape.com/author/Albert-Einstein/'
    response = requests.get(URL)
    if response.status_code == 200:
        html_tree = BeautifulSoup(response.text, "html.parser")
        n = html_tree.find("h3", attrs={"class": "author-title"}).text
        name = n[:15]
        birth_date = n[16:37]
        description = html_tree.find("div", attrs={"class": "author-description"}).text.strip()

        text_json = {
            "name": name,
            "birth_date": birth_date,
            "description": description
        }

        with open("info.json", "w") as f:
            json.dump(text_json, f, indent=4)
    else:
        print("error")
