from flask import Flask, request

app = Flask(__name__)

@app.route('/detection/<string:alert_id>', methods=['POST'])
def receber_alerta(alert_id):
    print(f"[Alerta recebido] ID: {alert_id}")
    dados = request.data.decode('utf-8')
    print("Conteúdo recebido:\n", dados)
    return "Alerta recebido com sucesso", 200

@app.route('/', methods=['GET'])
def home():
    return "Servidor Flask para receber alertas da Hikvision está online!", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render usa variável PORT
    app.run(host='0.0.0.0', port=port)
