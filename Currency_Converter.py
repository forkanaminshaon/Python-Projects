class CurrrencyConverter:


#class attribute #base value dollar
exchange_rates= {

    "USD" : 1.0, #BASE VALUE
    "BDT" : 121.75,
    "EUR" : 0.88,
    "GBP" : .75,
}

#Crate a object 
def __init__(self, amount, from_currency , to_currency):
self.amount =  amount #instance attribute 
self.from_currency = from_currency #BDT
self.to.currency = to_currency #usd

#(100, "BDT", "USD")

#instance method handle conversion
def convert (self):
    if self.from_currency not in CurrencyConverter.exchange_rates or \
    self.to_currency not in CurrencyConverter.exchange_rates:
    return "Invalid currency not in our system "

base_amount = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
Converted_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency]
return round (converted_amount,2)

(currency, new rate)

@classmethod
def update_rate(cls,currency, new_rate):



