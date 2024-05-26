from flask_restx import Namespace, fields
from api.schemas import FrequenciaProfessorTurmaMateriaSchema

frequencia_ns = Namespace('frequencias', description='Operações relacionadas a Frequências')

frequencia_model = frequencia_ns.model('FrequenciaProfessorTurmaMateria', {
    'plano_id': fields.Integer(required=True, description='ID do Plano Semanal do Bimestre'),
    'data': fields.Date(required=True, description='Data da Frequência'),
    'presente': fields.Boolean(description="Flag para registrar presenca")
})

frequencia_schema = FrequenciaProfessorTurmaMateriaSchema()
