import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/bitcoin/markets/' # $BTC value
url_ = 'https://valor.globo.com/valor-data/' # Price of Dolar in real 

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

print("valor do #BTC:: $", normalize(url))
print("Valor do dolar :: R$", normalize_dolar(url_))
