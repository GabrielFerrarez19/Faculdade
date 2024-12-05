from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Caminho para o arquivo JSON
DATA_FILE = "data.json"

# Função para carregar dados do JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Função para salvar dados no JSON
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)

@app.route('/save_data', methods=['POST'])
def save_data_route():
    new_entry = request.json
    data = load_data()
    data.append(new_entry)
    save_data(data)
    return jsonify({"message": "Dados salvos com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
