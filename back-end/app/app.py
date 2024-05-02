from flask import Flask
from flask_restx import Api
from flask_apispec import FlaskApiSpec
from app.config import Config
from app.config.database import db
from app.routes import register_routes
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialização do banco de dados
    with app.app_context():
        db.init_app(app)
        db.create_all()

    
    migrate = Migrate(app, db)

    # Configuração do Flask-RESTX
    api = Api(app, version='1.0', title='Minha API Escola',
              description='API para gerenciar informações escolares')

    # Configuração do Flask-apispec para geração de documentação do Swagger
    app.config['APISPEC_SPEC'] = FlaskApiSpec(app)
    app.config['APISPEC_SWAGGER_URL'] = '/swagger/'  # Endpoint para a interface do Swagger

    # Registre os blueprints
    register_routes(app)

    return app
