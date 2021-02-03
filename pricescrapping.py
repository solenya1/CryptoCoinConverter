import requests
from bs4 import BeautifulSoup

# that works!!
url = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

value = soup.find("div", {"class":"priceValue___11gHJ"})

print(value)

#Trying to get only value.

value_ = value.contents[0] # OK, now here i have only the value!

print(value_)

# Let's try to make it an integer value
value_ = value_.replace('$', "")
value_ = value_.replace(',', "")

value_type = type(value_)
print('\n')
print(value_)
print(value_type)

print('\n')

newvalue_ = float(value_)
print(newvalue_)
print(type(newvalue_)) # yeah it's work !!

# Try to transpose it into an function

