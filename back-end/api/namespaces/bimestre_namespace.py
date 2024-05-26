from flask_restx import Namespace, fields
from api.schemas import BimestreSchema

bimestre_ns = Namespace('bimestres', description='Operações relacionadas a Bimestres')

bimestre_model = bimestre_ns.model('Bimestre', {
    'descricao': fields.String(required=True, description='Descrição do Bimestre'),
    'data_inicio': fields.Date(required=True, description='Data de Início do Bimestre'),
    'data_fim': fields.Date(required=True, description='Data de Fim do Bimestre')
})

bimestre_schema = BimestreSchema()
