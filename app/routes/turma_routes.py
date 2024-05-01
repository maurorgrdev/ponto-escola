from flask import Blueprint
from flask_restx import Api
from app.controllers.turma_controller import TurmaController, TurmaList
from app.namespaces import turma_ns

def create_turma_blueprint():
    turma_bp = Blueprint('turma_bp', __name__)
    api = Api(turma_bp)
    api.add_namespace(turma_ns)
    api.add_resource(TurmaController, '/turmas/<int:id>')
    api.add_resource(TurmaList, '/turmas')
    return turma_bp
