from flask import Blueprint
from flask_restx import Api
from app.controllers.professor_controller import ProfessorController, ProfessorList  # Importe os controllers de Professor
from app.namespaces import professor_ns  # Importe o namespace de Professor

def create_professor_blueprint():
    professor_bp = Blueprint('professor_bp', __name__)
    api = Api(professor_bp)
    api.add_namespace(professor_ns)
    api.add_resource(ProfessorController, '/professores/<int:id>')  # Defina o endpoint para o controller de Professor
    api.add_resource(ProfessorList, '/professores')  # Defina o endpoint para a lista de professores
    return professor_bp
