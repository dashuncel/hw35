import osa
import requests
import statistics
import xml.etree.ElementTree as ET

'''
Дано: семь значений температур по Фаренгейту в файле temps.txt. 
Необходимо вывести среднюю за неделю арифметическую температуру по Цельсию.
'''
URI = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'

# via requests
def get_celsius_request(**params):
    if params['unit'] != "F":
        return params['degree']
    headers = {'Content-Type': 'text/xml'}
    data = f'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{params['degree']}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>
'''
    resp = requests.post(URI, headers=headers, data=data)
    tree = ET.fromstring(resp.content)
    return(float(tree[0][0][0].text))


def readFile(fileName='temps.txt'):
    celsius = []
    try:
        with open(fileName, 'r') as f:
            for line in f:
                celsius.append({'degree': int(line.split(' ')[0].strip()),
                                'unit': line.split(' ')[1].strip()})

    except FileNotFoundError as e:
        print(f'file {fileName} NOT found')
    except IOError as e:
        print(f'I/O error({e.errno}): {e.strerror}')
    except:
        print(f'Unexpected error: {sys.exc_info()[0]}')
        raise
    return celsius


celsius = list(map(lambda f: get_celsius_request(**f), readFile()))
print(celsius)
print('Средняя температура за неделю:', round(statistics.mean(celsius), 2))

