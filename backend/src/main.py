from flask import Flask
from flask_cors import CORS
import sys
import os

# Adiciona o diretório pai ao path para importar o módulo app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from app.main import app
except ImportError:
    # Se não conseguir importar, cria uma app Flask básica
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')
    def hello():
        return {"message": "Budget Calculator API is running!"}
    
    @app.route('/health')
    def health():
        return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

