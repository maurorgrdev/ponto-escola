from marshmallow import Schema, fields, validate, ValidationError
from .materia_schema import MateriaSchema
from .turma_schema import TurmaSchema
from app.models import Materia, Turma
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
    turma = fields.Nested(TurmaSchema, attribute='turma_obj', dump_only=True)
    materia = fields.Nested(MateriaSchema, attribute='materia_obj', dump_only=True)

    # Método para carregar dados do objeto TurmaMateria
    @staticmethod
    def get_instance(data):
        return {
            'id_turma': data.get('id_turma'),
            'id_materia': data.get('id_materia')
            # Adicione mais campos conforme necessário
        }

    # Método para validar a existência de uma matéria associada
    @staticmethod
    def validate_materia_exists(value):
        materia_id = value.get('id_materia')
        if not materia_id:
            raise ValidationError('ID da matéria é obrigatório')

        if not Materia.query.get(materia_id):
            raise ValidationError(f'Matéria com ID {materia_id} não encontrada')

    # Método para validar a existência de uma turma associada
    @staticmethod
    def validate_turma_exists(value):
        turma_id = value.get('id_turma')
        if not turma_id:
            raise ValidationError('ID da turma é obrigatório')

        if not Turma.query.get(turma_id):
            raise ValidationError(f'Turma com ID {turma_id} não encontrada')
