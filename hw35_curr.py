import osa
import requests

URI = "http://fx.currencysystem.com/webservices/CurrencyServer4.asmx"

amt = []
with open('currencies.txt', 'r') as f:
    for line in f:
        curr = line.split(' ')[2].strip()
        amount = int(line.split(' ')[1].strip())
        print(curr, amount)


