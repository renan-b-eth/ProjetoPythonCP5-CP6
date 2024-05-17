#!pip install unidecode
#!pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import warnings

def soup_praias():
# URL da página que você deseja consumir
    url = 'https://praialimpa.net/sao-paulo/'

    #Lista de praias para buscar
    praias = ["Ubatuba, Caraguatatuba", "São Sebastião", "Ilhabela", "Bertioga", "Guarujá", "Santos", "São Vicente", "Praia Grande", "Mongaguá", "Itanhaéma", "Peruíbe", "Ilha Comprida", "Cubatão"]

    #Para ignorar o aviso de warnings
    warnings.filterwarnings("ignore", message="Unverified HTTPS request")

    response = requests.get(url, verify=False)
    response.encoding = 'UTF-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('section')
        for p in paragraphs:
            texto_formatado = p.text.replace('Própria', 'Própria - ').replace('Imprópria', 'Imprópria - ')
            for praia in praias:
                if praia in texto_formatado:
                    # trocar para um dicionário onde nome da praia é chave e a balneabilidade o valor
                    print(texto_formatado)
                    break

    else:
        print(f"Erro ao acessar a página: {response.status_code}")
    return ""

def busca_praia(soup_praias):
     praia = input()

    # buscar dentro do dicionário
     if praia in soup_praias:
        return None

