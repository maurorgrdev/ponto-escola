from marshmallow import Schema, fields, validate, ValidationError
from .materia_schema import MateriaSchema
from .turma_schema import TurmaSchema
from api.models import Materia, Turma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class TurmaMateriasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Turma
        load_instance = True

    materias = fields.Nested('MateriaSchema', many=True)

class MateriaTurmasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Materia
        load_instance = True

    turmas = fields.Nested('TurmaSchema', many=True)


class TurmaMateriaSchema(Schema):
    id = fields.Integer(dump_only=True)
    id_turma = fields.Integer(required=True)
    id_materia = fields.Integer(required=True)