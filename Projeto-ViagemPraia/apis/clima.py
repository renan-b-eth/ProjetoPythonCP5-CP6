import requests
from datakeys import key_clima

def api_clima(cidade):
    
    api_key = key_clima #chave da api está nas anotações

    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
            data = response.json()
            temp = round((data['main']['temp']-273.15))
            temp_min = round((data['main']['temp_min']-273.15))
            temp_max = round((data['main']['temp_max']-273.15))
            print(f'Previsão do tempo para {cidade}')
            print(f'Atual: {temp}°C')
            print(f'Máxima do dia: {temp_max}°C')
            print(f'Mínima do dia: {temp_min}°C')
            return temp, temp_max, temp_min, cidade
    else:
            print('Error fetching weather data')
    