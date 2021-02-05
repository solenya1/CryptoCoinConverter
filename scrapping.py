import requests
from bs4 import BeautifulSoup


def normalize(link):

    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    value = soup.find("div", {"class":"priceValue___11gHJ"})
    value_ = value.contents[0]
    value_ = value_.replace('$', "")
    value_ = value_.replace(',', "")
    newvalue_ = float(value_)

    return newvalue_


def normalize_dolar(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    value = soup.find("div", {"class":"cell auto data-cotacao__ticker_quote"})
    value_ = value.contents[0]
    value_ = value_.replace(',', '.')
    newvalue = float(value_)

    return newvalue 

