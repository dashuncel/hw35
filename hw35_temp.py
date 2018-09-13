import osa
import requests
import statistics

'''
Дано: семь значений температур по Фаренгейту в файле temps.txt. 
Необходимо вывести среднюю за неделю арифметическую температуру по Цельсию.
'''
URI = 'https://www.w3schools.com/xml/tempconvert.asmx'

# via osa
def get_celsius(fahrenheit):
    client = osa.Client(URI)
    resp = client.service.FahrenheitToCelsius(fahrenheit)
    print(resp)
    return 1 # заглушка пока не работает сервис

# via requests
def get_celsius_request(fahrenheit):
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    data = f'''
            <?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
                    <Fahrenheit>{fahrenheit}</Fahrenheit>
                </FahrenheitToCelsius>
            </soap:Body>
            </soap:Envelope>
            '''

    resp = requests.post(URI + '?WSDL', headers=headers, data=data)
    print(resp)
    return 2 # заглушка пока не работает сервис


celsius = []
with open('temps.txt', 'r') as f:
    for line in f:
        line = line.split(' ')[0].strip()
        #celsius.append(print(get_celsius(line)))
        celsius.append(int(get_celsius_request(line)))


print('Средняя температура за неделю:', statistics.mean(celsius))

