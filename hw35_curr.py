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

def getRubAmount(**params):
    client = osa.Client(URI)
    resp = client.service.ConvertToNum(toCurrency="RUB", fromCurrency=params['curr'], amount=params['amt'], rounding=True)
    return resp

def readFile(fileName='currencies.txt'):
    amt = []
    try:
        with open(fileName, 'r') as f:
            for line in f:
                curr = line.split(' ')[2].strip()
                amount = float(line.split(' ')[1].strip())
                amt.append({'curr': curr, 'amt': amount})
    except FileNotFoundError as e:
        print(f'fle {fileName} NOT found')
    except IOError as e:
        print(f'I/O error({e.errno}): {e.strerror}')
    except:
        print(f'Unexpected error: {sys.exc_info()[0]}')
        raise

    return amt


consumption = list(map(lambda f: getRubAmount(**f), readFile()))
print(f'Сумма затрат на поездку по курсу на {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} = ', round(sum(consumption)))

