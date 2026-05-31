from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "proyecto": "Veridia",
        "estado": "Backend configurado correctamente",
        "tecnologias": ["Python", "Flask", "Supabase", "Firebase"]
    })

if __name__ == '__main__':
    # Usa el puerto 5000 por defecto
    app.run(debug=True, port=5000)