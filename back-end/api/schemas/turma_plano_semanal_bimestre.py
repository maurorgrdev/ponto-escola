# schemas/turma_plano_semanal_bimestre.py

from marshmallow import Schema, fields

class TurmaPlanoSemanalBimestreSchema(Schema):
    id = fields.Int(dump_only=True)
    turma_id = fields.Int(required=True)
    dia_semana = fields.Str(required=True)
    bimestre_id = fields.Int(required=True)
    tempo_id = fields.Int(required=True)
    materia_id = fields.Int(required=True)
    professor_id = fields.Int(required=True)
