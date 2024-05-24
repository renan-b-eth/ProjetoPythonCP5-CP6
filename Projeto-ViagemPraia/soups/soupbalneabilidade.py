#!pip install unidecode
#!pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import warnings


# URL da página que você deseja consumir
url = 'https://praialimpa.net/sao-paulo/'

# Lista de praias para buscar
praias = ["Ubatuba, Caraguatatuba", "São Sebastião", "Ilhabela", "Bertioga", "Guarujá", "Santos", "São Vicente", "Praia Grande", "Mongaguá", "Itanhaéma", "Peruíbe", "Ilha Comprida", "Cubatão"]

# Para ignorar o aviso de warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

response = requests.get(url, verify=False)
response.encoding = 'UTF-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('section')

    # Dicionário final para armazenar todas as praias e suas condições
    dicionario_final = {}
    dic = {}
    dic3 = {}
    dicformatado = {}

    for p in paragraphs:
        texto_formatado = p.text.replace('Própria', 'Própria - ').replace('Imprópria', 'Imprópria - ')
        texto_formatado2 = texto_formatado.replace('\n', ' - ')
        dic3[texto_formatado2] = texto_formatado
        print(dic3)
        propria = texto_formatado.split(" - ")[0]
        proria2 = propria.replace('\n', ' - ')
        nome_da_praia = texto_formatado.split(" - ")[1]
        nome_praia_certo = nome_da_praia.replace('\xa0', '')
        dic[nome_praia_certo] = proria2
        ultimo_valor_dic =  list(dic.values())[-1]
        dic3 = {}
        dic3[nome_praia_certo] = ultimo_valor_dic
        #dic3.values() para puxar os valores
        # list(dic3.values())[0] puxa o valor especifico
        

        for praia in praias:
            if praia in texto_formatado:
                palavras = texto_formatado.splitlines()

                for linha in palavras:
                    if linha.startswith("Imprópria") or linha.startswith("Própria"):
                        palavra_impropria_propria = linha.split(" - ")[0]
                        nome_da_praia = linha.split(" - ")[1]
                        nome_praia2 = nome_da_praia.replace('\xa0', '')

                        # Atualiza o dicionário final com a condição da praia
                        dicionario_final[nome_praia2] = palavra_impropria_propria
                      
                        break
    # Imprime o dicionário final
    #print(dicionario_final)            
    
else:
    print(f"Erro ao acessar a página: {response.status_code}")

def busca_praia(dicionario_final):
    
    praia = input("digite")

    #value_key={}
    #limpeza = []
    for key, value in dicionario_final.items():
        print('ola')
        print(dicionario_final[f'{praia}'])


busca_praia(dicionario_final)