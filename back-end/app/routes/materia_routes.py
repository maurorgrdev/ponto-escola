from flask import Blueprint
from flask_restx import Api
from app.controllers.materia_controller import MateriaController, MateriaList
from app.namespaces import materia_ns

def create_materia_blueprint():
    materia_bp = Blueprint('materia_bp', __name__)
    api = Api(materia_bp)
    api.add_namespace(materia_ns)
    api.add_resource(MateriaController, '/materias/<int:id>')
    api.add_resource(MateriaList, '/materias')
    return materia_bp
