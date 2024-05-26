from flask_restx import Namespace, fields
from api.schemas import TempoSchema

tempo_ns = Namespace('tempos', description='Operações relacionadas a Tempos')

tempo_model = tempo_ns.model('tempo', {
    'descricao': fields.String(required=True, description='Descrição do Tempo'),
    'horario_inicio': fields.String(required=True, description='Horário de Início'),
    'horario_fim': fields.String(required=True, description='Horário de Fim')
})

tempo_schema = TempoSchema()
