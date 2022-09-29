import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://rezka.ag/films/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="b-content__inline_item")
    film = []
    for i in items:
        film.append({
            "title": i.find("div", class_='b-content__inline_item-link').find("a").getText(),
            "info": i.find("div", class_='b-content__inline_item-link').find("div").getText().split(', '),
            "sylka": i.find("div", class_='b-content__inline_item-link').find("a").get("href"),
        })
    return film


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = get_data(html.text)
        return answer
    else:
        raise Exception("ошибка при парсинге")


pprint(parser())
