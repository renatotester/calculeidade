from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    data_nasc = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    return idade

@app.route('/api/v1/calcule', methods=['POST'])
def calcule_idade():
    try:
        dados = request.get_json()
        print('dados')
        # Validar se todos os parâmetros foram fornecidos
        # CHAMAR EM CURL PELO POST OS DADOS
        if not all(key in dados for key in ['nome', 'data_nascimento']):
            return jsonify({"error": "Todos os parâmetros são obrigatórios"}), 400

        nome = dados['nome']
        data_nascimento = dados['data_nascimento']

        # Validar o formato da data de nascimento
        try:
            datetime.strptime(data_nascimento, '%d/%m/%Y')
        except ValueError:
            return jsonify({"error": "Formato de data inválido. Use o formato DD/MM/AAAA"}), 400

        idade = calcular_idade(data_nascimento)

        return jsonify({"msg": f"{nome}, sua idade é {idade} anos"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
        print(request.base_url)
        idade = calcular_idade('22/05/1985')
        print(idade)    
        return str(idade), 201

if __name__ == '__main__':
    app.run(debug=True)


