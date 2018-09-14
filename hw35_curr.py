import osa
import datetime

'''
Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты. 
Даны цены на билеты в местных валютах (файл currencies.txt). Формат данных в файле:

<откуда куда>: <стоимость билета> <код валюты>
Пример:

MOSCOW-LONDON: 120 EUR
Посчитайте, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).
'''

URI = "http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL"

def getRubAmount(fromCurr, amt):
    client = osa.Client(URI)
    resp = client.service.ConvertToNum(toCurrency="RUB", fromCurrency=fromCurr, amount=amt, rounding=True)
    return resp

amt = []# список сумм в рублях

with open('currencies.txt', 'r') as f:
    for line in f:
        curr = line.split(' ')[2].strip()
        amount = float(line.split(' ')[1].strip())
        amt.append(getRubAmount(curr, amount))

print(f'Сумма затрат на поездку по курсу на {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} = ', round(sum(amt)))

