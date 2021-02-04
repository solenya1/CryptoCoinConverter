import requests
from bs4 import BeautifulSoup


url = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
    
def normalize(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    value = soup.find("div", {"class":"priceValue___11gHJ"})

    value_ = value.contents[0]

    value_ = value_.replace('$', "")
    value_ = value_.replace(',', "")

    newvalue_ = float(value_)

    return newvalue_


print(normalize(url))
