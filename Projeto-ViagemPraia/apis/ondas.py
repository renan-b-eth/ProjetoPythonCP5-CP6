import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def buscar_id_cidade(cidade):
    url = f"https://brasilapi.com.br/api/cptec/v1/cidade/{cidade}"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        try:
            id_cidade = response.json()
            return id_cidade[0]['id']
        except KeyError:
            print(f"Erro ao buscar ID da cidade: {cidade}")
            return None
    else:
        print(f"Falha ao buscar cidade: {cidade} (código de status: {response.status_code})")
        return None

def consumir_api(nome_cidade, dias):
    id_cidade = buscar_id_cidade(nome_cidade)
    if id_cidade:
        url = f"https://brasilapi.com.br/api/cptec/v1/ondas/{id_cidade}/{dias}"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Falha ao consumir API para a cidade {nome_cidade} (código de status: {response.status_code})")
            return None
    else:
        print("Cidade não encontrada. Por favor, verifique o nome da cidade.")
        return None

nome_cidade = input("Digite cidade:")
dias = int(input("Quantidade de dias:"))

user_data = consumir_api(nome_cidade, dias)
if user_data:
    # Extraindo as chaves "vento" e "altura_onda" dos dados
    for onda in user_data['ondas'][0]['dados_ondas']:
        print(f"Hora: {onda['hora']}, Vento: {onda['vento']}, Altura Onda: {onda['altura_onda']}")
else:
    print("Erro ao obter dados. Por favor, verifique o nome da cidade e a quantidade de dias.")