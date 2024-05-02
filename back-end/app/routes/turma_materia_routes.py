from flask import Blueprint
from flask_restx import Api
from app.controllers.turma_materia_controller import TurmaMateriaController, \
    TurmaMateriaList, TurmaMateriaListByTurma, MateriaTurmaListByMateria  # Importe os controllers de TurmaMateria
from app.namespaces import turma_materia_ns  # Importe o namespace de TurmaMateria

def create_turma_materia_blueprint():
    turma_materia_bp = Blueprint('turma_materia_bp', __name__)
    api = Api(turma_materia_bp)
    api.add_namespace(turma_materia_ns)

    api.add_resource(TurmaMateriaController, '/turmas-materias/<int:id>')
    
    api.add_resource(TurmaMateriaList, '/turmas-materias')

    # Adicionando endpoint para buscar matérias de uma turma específica
    api.add_resource(TurmaMateriaListByTurma, '/turmas/<int:id_turma>/materias')

    # Adicionando endpoint para buscar turmas de uma materia específica
    api.add_resource(MateriaTurmaListByMateria, '/materias/<int:id_materia>/turmas')

    return turma_materia_bp
