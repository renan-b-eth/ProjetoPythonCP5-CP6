from flask import Flask, render_template, request
import requests
from apis.clima import api_clima
app = Flask(__name__, static_url_path='/templates')

@app.route('/')
def home():
    #cidade = request.form['cidade']
    return render_template('index.html')
    #return render_template('index.html', api_clima(cidade))

@app.route('/enviar-cidade', methods=['POST'])
def getcidade():
    cidade = request.form['cidade']
    temperatura= api_clima(cidade)
    return render_template('index.html', temperatura= temperatura)


if __name__ == '__main__':
    app.run()