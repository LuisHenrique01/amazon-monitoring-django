import re
import requests
from bs4 import BeautifulSoup as bs
from . import HEADERS, BASE_URL, RE_ASIN, RE_PRICE


def get_name(url: str) -> str:
    response = requests.get(url, headers=HEADERS)
    soup = bs(response.content, 'html.parser')
    soup = bs(soup.prettify(), 'html.parser')
    title = soup.find('span', id='productTitle')
    return title.text


def get_asin(url: str) -> str:
    asin = re.findall(RE_ASIN, url)[0]
    return asin


def get_price(asin: str) -> float:
    unic_url = BASE_URL + 's?k=' + asin
    response = requests.get(unic_url, headers=HEADERS)
    soup = bs(response.content, 'html.parser')
    soup = bs(soup.prettify(), 'html.parser')
    spans = soup.find_all('span', class_='a-price')
    price = re.findall('\d+[.,]\d+[.,]\d+|\d+[.,]\d+',
                       spans[0].text.strip())[0]
    sep = price[-3]
    if sep == ',':
        price = price.replace('.', '')
        price = price.replace(',', '.')
    elif sep == '.':
        price = price.replace(',', '')
    else:
        price = price.replace(',', '').replace('.', '')
    return float(price)
