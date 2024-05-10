import csv
from flask import Flask, jsonify, request, abort
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)  # Configura CORS para todas as rotas

@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensagem': 'Bem vindo a API de pesquisa'})

@app.route('/pesquisa', methods=['POST'])
def realizar_pesquisa():
    # Validação dos dados de entrada
    if not request.json or not all(k in request.json for k in ['email', 'marca', 'cor', 'valor', 'carro']):
        abort(400, description="Missing data in request")  # Retorna 400 Bad Request se algum dado faltar
        
    data = request.get_json()
    email = data['email']
    marca = data['marca']
    cor = data['cor']
    valor = data['valor']
    carro = data['carro']
    salvar_pesquisa(email, marca, cor, valor, carro)
     
    return jsonify({'mensagem': 'Pesquisa salva com sucesso!'})


@app.route('/pesquisa', methods=['GET'])
def get_todas_pesquisas():
    pesquisa = []
    try:
        with open('pesquisas-api.csv', 'r', newline='') as arquivo:
            tabela = csv.reader(arquivo)
            for row in tabela:
                pesquisa.append({'email': row[0], 'marca': row[1], 'cor': row[2], 'valor': row[3], 'carro': row[4]})
    except FileNotFoundError:
        abort(404, description="No data found")

    return jsonify(pesquisa)

@app.route('/pesquisa/<email>', methods=['GET'])
def get_pesquisa_email(email):
    try:
        with open('pesquisas-api.csv', 'r', newline='') as arquivo:
            tabela = csv.reader(arquivo)
            for row in tabela:
                if row[0] == email:
                    return jsonify({'email': row[0], 'marca': row[1], 'cor': row[2], 'valor': row[3], 'carro': row[4]})
    except FileNotFoundError:
        abort(404, description="No data found")
    
    abort(404, description="Research not found for the given email")



def salvar_pesquisa(email, marca, cor, valor, carro):
    with open('pesquisas-api.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([email, marca, cor, valor, carro])

if __name__ == '__main__':
    app.run(debug=True)
