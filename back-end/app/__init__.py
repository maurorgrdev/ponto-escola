import os
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from .configuration import Config
from .configuration import db
from .route import register_routes

# Carregar variáveis de ambiente do .env
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        # db.drop_all()
        db.create_all()

    api = Api(app, version='1.0', title='My API',
              description='Esta é a API de Gerenciamento de Frequência Escolar',
              doc='/swagger/')

    register_routes(api, app)

    return app
