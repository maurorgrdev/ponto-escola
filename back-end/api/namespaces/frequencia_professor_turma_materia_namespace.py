from flask_restx import Namespace, fields
from api.schemas.frequencia_professor_turma_materia_schema import FrequenciaProfessorTurmaMateriaSchema

frequencia_professor_turma_materia_ns = Namespace('frequencia-professor-turma-materia', description='Operações relacionadas a presença do professor')

frequencia_professor_turma_materia_model = frequencia_professor_turma_materia_ns.model('', {
    'professor_id': fields.Integer(required=True, description=''),
    'data': fields.Date(required=True, description=''),
    'materia_id': fields.Integer(required=True, description=''),
    'turma_id': fields.Integer(required=True, description=''),
    'presente': fields.Boolean(required=True, description='')
})