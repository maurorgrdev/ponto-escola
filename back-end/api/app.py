from flask import Flask, Blueprint
from flask_restx import Api
from api.config import Config
from api.config.database import db
from api.routes import register_routes
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialização do banco de dados
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

    migrate = Migrate(app, db)

     # Initialize Flask-Restx Api
    api = Api(app, version='1.0', title='API Documentation', description='API Documentation')

    # Add namespaces to the API
    register_routes(api)

    return app
