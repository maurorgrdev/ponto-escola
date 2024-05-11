
from api.schemas import TurmaSchema
from flask_restx import Namespace, fields

turma_ns = Namespace('turmas', description='Operações relacionadas a turma')

turma_schema = TurmaSchema()

turma_model = turma_ns.model('Turma', {
    'nome': fields.String,
})
