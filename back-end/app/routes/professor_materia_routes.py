# professor_materia_routes.py

from flask import Blueprint
from flask_restx import Api
from app.controllers.professor_materia_controller import ProfessorMateriaController, ProfessorMateriaList, ProfessorMateriaListByProfessor, MateriaProfessorListByMateria  # Importe os controllers de ProfessorMateria
from app.namespaces import professor_materia_ns  # Importe o namespace de ProfessorMateria

def create_professor_materia_blueprint():
    professor_materia_bp = Blueprint('professor_materia_bp', __name__)
    api = Api(professor_materia_bp)
    api.add_namespace(professor_materia_ns)
    
    # Adicionando endpoints para o controlador ProfessorMateriaController
    api.add_resource(ProfessorMateriaController, '/professores-materias/<int:id>')
    
    # Adicionando endpoints para o controlador ProfessorMateriaList
    api.add_resource(ProfessorMateriaList, '/professores-materias')
    
    # Adicionando endpoint para buscar matérias de um professor específico
    api.add_resource(ProfessorMateriaListByProfessor, '/professores/<int:id_professor>/materias')

    # Adicionando endpoint para buscar professores de uma matéria específica
    api.add_resource(MateriaProfessorListByMateria, '/materias/<int:id_materia>/professores')

    return professor_materia_bp
