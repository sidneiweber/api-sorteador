# Importando bibliotecas
from flask import Flask, jsonify, request
from random import randint
from datetime import datetime

# Criar flask app
app = Flask(__name__)

@app.route('/')
def home():
    pessoas = request.args.get('pessoas', default=10, type=int)
    sorteados = request.args.get('sorteados', default=1, type=int)
    data = datetime.now()
    numbers = set()
    while len(numbers) < sorteados:  # enough is defined somewhere...
        numbers.add(randint(0, pessoas))
    s = list(numbers)

    return jsonify({'numeros_sorteados': s, 'data': data.strftime('%d/%m/%Y %H:%M')})

if __name__ == '__main__':
    app.run(debug=True)
