import requests

def api_clima():
    
    api_key = '' #chave da api está nas anotações

    city = input('Enter city name: ')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
            data = response.json()
            temp = round((data['main']['temp']-273.15))
            temp_min = round((data['main']['temp_min']-273.15))
            temp_max = round((data['main']['temp_max']-273.15))
            print(f'Previsão do tempo para {city}')
            print(f'Atual: {temp}°C')
            print(f'Máxima do dia: {temp_max}°C')
            print(f'Mínima do dia: {temp_min}°C')
    else:
            print('Error fetching weather data')
    
print(api_clima())