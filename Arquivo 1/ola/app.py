from flask import Flask, render_template, request,url_for
import requests
from key import api_key
import bs4


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contato')
def contato():
  return render_template('contato.html',usuario = 'Junior')


@app.route('/noticias')
def raspa_veja():
    response = requests.get('https://veja.abril.com.br/')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    mais_lidas = soup.find_all('section', {'class': 'block most-read dark'})
    conteudos = mais_lidas[0].find_all('div', {'class': 'our-carousel-item'})
    noticias = []

    for conteudo in conteudos:
        titulo = conteudo.find('h2').text
        link = conteudo.find('a').get('href')
        noticias.append(f"{titulo}\n{link}")
    return render_template('noticias.html', resultado = "\n\n".join(noticias))

# @app.route('/clima')
# def clima():
#     return render_template('clima.html')


# Rota que processa os dados enviados pelo formulário
@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    return f'Olá {nome}, seu email {email} foi recebido com sucesso!'


@app.route('/clima', methods=['POST', 'GET'])
def clima():
    if request.method == 'POST':
        try:
            cidade = request.form['cidade']
            apikey = api_key  # Substitua com sua chave API real
            url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={apikey}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            clima = response.json()
            temperatura = clima['main']['temp']
            return render_template('clima.html', temperatura=temperatura)
        except requests.RequestException as e:
            return render_template('clima.html', error=str(e))
    return render_template('clima.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)