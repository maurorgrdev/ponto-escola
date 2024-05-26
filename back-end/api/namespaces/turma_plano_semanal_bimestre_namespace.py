# namespaces/turma_plano_semanal_bimestre_namespace.py

from flask_restx import Namespace, fields
from api.schemas.turma_plano_semanal_bimestre import TurmaPlanoSemanalBimestreSchema

turma_plano_ns = Namespace('turma_plano_semanal_bimestre', description='Operações relacionadas a Turma Plano Semanal Bimestre')

# Definição do modelo de Turma Plano Semanal Bimestre
turma_plano_model = turma_plano_ns.model('TurmaPlanoSemanalBimestre', {
    'id': fields.Integer(readonly=True),
    'turma_id': fields.Integer(required=True),
    'dia_semana': fields.String(required=True),
    'bimestre_id': fields.Integer(required=True),
    'tempo_id': fields.Integer(required=True),
    'materia_id': fields.Integer(required=True),
    'professor_id': fields.Integer(required=True)
})

# Esquema para serialização/deserialização
turma_plano_semanal_bimestre_schema = TurmaPlanoSemanalBimestreSchema()
