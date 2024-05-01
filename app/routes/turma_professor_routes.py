from flask import Blueprint
from flask_restx import Api
from app.controllers.turma_professor_controller import TurmaProfessorController, \
    TurmaProfessorList, TurmaProfessorListByTurma, ProfessorTurmaListByProfessor
from app.namespaces import turma_professor_ns  # Importe o namespace de TurmaProfessor

def create_turma_professor_blueprint():
    turma_professor_bp = Blueprint('turma_professor_bp', __name__)
    api = Api(turma_professor_bp)
    api.add_namespace(turma_professor_ns)

    api.add_resource(TurmaProfessorController, '/turmas-professores/<int:id>')
    
    api.add_resource(TurmaProfessorList, '/turmas-professores')
    
        # Adicionando endpoint para buscar professores de uma turma específica
    api.add_resource(TurmaProfessorListByTurma, '/turmas/<int:id_turma>/professores')

    # Adicionando endpoint para buscar turmas de uma professor específico
    api.add_resource(ProfessorTurmaListByProfessor, '/professores/<int:id_professor>/turmas')


    return turma_professor_bp
