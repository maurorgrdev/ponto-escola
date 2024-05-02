# run.py

import argparse
from app.app import create_app
import time  # Importe o módulo time

# Parse dos argumentos de linha de comando
parser = argparse.ArgumentParser(description='Run the Flask application.')
parser.add_argument('--host', default='0.0.0.0', help='Host address to run the application on')  # Adicione um argumento para o host
parser.add_argument('--port', type=int, default=9001, help='Port number to run the application on')
args = parser.parse_args()

# Crie o aplicativo Flask
app = None

# Tente criar o aplicativo Flask várias vezes até que a conexão com o banco de dados seja estabelecida
for attempt in range(1, 6):  # Faça 5 tentativas
    try:
        app = create_app()
        break  # Se a criação do aplicativo for bem-sucedida, saia do loop
    except Exception as e:
        print(f"Attempt {attempt}: Error creating app: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)  # Espere 5 segundos antes de tentar novamente

# Se o aplicativo não puder ser criado após várias tentativas, encerre o script
if app is None:
    print("Failed to create app after multiple attempts. Exiting.")
    exit(1)

# Execute o aplicativo Flask no host e porta especificados
if __name__ == "__main__":
    app.run(host=args.host, port=args.port, debug=True)
