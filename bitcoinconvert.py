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


# Some random values
btc = 34413.46
dolar = 5.46
wallet_reais = 500
wallet_dolar = 500

# The Basics of the function
convert = Convert(btc_actual_price=btc, dolar_actual_price=dolar,
                    real_input=wallet_reais, dolar_input=wallet_dolar, btc_input=0)

# Testing the algorithm and it's WORK !!!
dolar_value = convert.real_to_dolar()
btc_value = convert.real_to_btc(dolar_value)

convert = Convert(btc_actual_price=btc, dolar_actual_price=dolar,
                    real_input=wallet_reais, dolar_input=wallet_dolar, btc_input=btc_value)

real_value = convert.btc_to_real()
dolar_value_ofbtc = convert.btc_to_dolar()


print(f'Valor em reais:: {wallet_reais} | valor em dolar :: {dolar_value} | valor em $BTC :: {btc_value}')

print(f'Valor em reais novamente convertidos : {real_value}')

print(f'Valor em dolar novamente convertidos: {dolar_value_ofbtc}')

"""

    Now it's time to take the data from internet process and see if we can get the real time 
    $BTC value to convert in the function, maybe trying some requests or Selenium 

"""
