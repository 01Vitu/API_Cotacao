from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/currency/<from_currency>/<to_currency>')
def get_currency_exchange_rate(from_currency, to_currency):
    url = 'https://api.exchangerate-api.com/v4/latest/{}'.format(from_currency.upper())
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][to_currency.upper()]
    return jsonify(exchange_rate=exchange_rate)

if __name__ == '__main__':
    app.run(debug=True)
