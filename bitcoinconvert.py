from scrapping import normalize
from scrapping import normalize_dolar

""" 
    Some information:

    btc_actual_price = it consist in the current price of the bitcoin that we will be
    looking for using requests and BeautifulSoup;
    dolar_actual_price = it's the current price of dolar to brazil currency
    real_input = it's the amount of cash that i'm want to convert;
    dolar_input = it's the amout of dolar that i want to convert if it's possible;
    btc_input = if you want to do de reverse process this allows do that.

    Why real_to_btc have the dolar_value ?
    R: Well, the current price of a bitcoin that we going to use is the same values of the 
    coinmarketplace so, to be easy is already in Dolar, so we convert the amount of real to
    dolar them to $BTC, yay!!!

"""
class Convert:
    
    def __init__(self, btc_actual_price, dolar_actual_price,
                 real_input=0, dolar_input=0, btc_input=0):
        
        self.btc = btc_actual_price
        self.dolar_price = dolar_actual_price
        self.myreal = real_input
        self.mydolar = dolar_input
        self.mybtc = btc_input
        
    def real_to_dolar(self):
        dolar_value = self.myreal / self.dolar_price
        return dolar_value
    
    def dolar_to_real(self):
        real_value = self.myreal * self.dolar_price
        return real_value
    
    def real_to_btc(self, dolar_value):
        btc_value = dolar_value / self.btc
        return btc_value

    def dolar_to_btc(self):
        btc_value = self.mydolar / self.btc
        return btc_value
    
    def btc_to_real(self):
        real_value = (self.mybtc * self.btc) * self.dolar_price
        return real_value

    def btc_to_dolar(self):
        dolar_value = self.mybtc * self.btc
        return dolar_value

# This links below it's where I collect the actual price fo $BTC and $USDolar.
url = 'https://coinmarketcap.com/currencies/bitcoin/markets/' # $BTC value
url_ = 'https://valor.globo.com/valor-data/' # Price of Dolar in real

# The input data.
btc = normalize(url)
dolar = normalize_dolar(url_)
wallet_reais = 0 
wallet_dolar = 0

# <---------------------------------------------------------------------------->
# TESTING THE PROGRAM

while True:
    print('--------------------------------')
    print('Welcome do CryptoCoinConverter')
    print('-------------------------------')
    print('Please Select your currency:')
    print('[1] $Dolar \n[2] $REAL \n[3] EXIT')
    print('\n')
    C = int(input('Type Here::'))

    if C == 1:
        pass
    if C == 2:
        pass
    if C == 3:
        print('-------------------------------------')
        print('         Thanks to utilize CCandC')
        break
