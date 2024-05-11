from flask import Flask, render_template, request
import requests
import clima

app = Flask(__name__)

@app.route('/')
def home():
    cidade = request.form['cidade']
    return render_template('index.html', api_clima(cidade))

if __name__ == '__main__':
    app.run()