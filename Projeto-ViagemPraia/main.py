from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    cidade = request.form['cidade']
    email = request.form['email']
    return render_template('index.html')

if __name__ == '__main__':
    app.run()