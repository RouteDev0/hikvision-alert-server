from flask import Flask, request

app = Flask(__name__)

@app.route("/detection/camera01", methods=["POST"])
def receber_alerta():
    print("📩 Alerta recebido!")
    print(request.data)
    return "OK", 200


@app.route('/', methods=['GET'])
def home():
    return "Servidor Flask para receber alertas da Hikvision está online!", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render usa variável PORT
    app.run(host='0.0.0.0', port=port)
