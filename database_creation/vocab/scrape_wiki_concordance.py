import requests
from bs4 import BeautifulSoup


def scrape_verses(link):
    r = requests.get(link)
    assert r.status_code == 200

    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)


if __name__ == "__main__":
    url = "https://en.m.wiktionary.org/wiki/Concordance:New_Testament_Greek"
    scrape_verses(url)