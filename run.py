# run.py

import argparse
from app.app import create_app

# Parse dos argumentos de linha de comando
parser = argparse.ArgumentParser(description='Run the Flask application.')
parser.add_argument('--host', default='0.0.0.0', help='Host address to run the application on')  # Adicione um argumento para o host
parser.add_argument('--port', type=int, default=9001, help='Port number to run the application on')
args = parser.parse_args()

# Crie o aplicativo Flask
app = create_app()

# Execute o aplicativo Flask no host e porta especificados
if __name__ == "__main__":
    app.run(host=args.host, port=args.port, debug=True)
