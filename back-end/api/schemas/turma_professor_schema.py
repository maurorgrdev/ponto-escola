# turma_professor_schema.py

from marshmallow import Schema, fields, validate, ValidationError
from .professor_schema import ProfessorSchema
from .turma_schema import TurmaSchema
from api.models import Professor, Turma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class TurmaProfessoresSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Turma
        load_instance = True

    professores = fields.Nested('ProfessorSchema', many=True)

class ProfessorTurmasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Professor
        load_instance = True

    turmas = fields.Nested('TurmaSchema', many=True)

class TurmaProfessorSchema(Schema):
    id = fields.Integer(dump_only=True)
    id_turma = fields.Integer(required=True)
    id_professor = fields.Integer(required=True)
    turma = fields.Nested(TurmaSchema, attribute='turma_obj', dump_only=True)
    professor = fields.Nested(ProfessorSchema, attribute='professor_obj', dump_only=True)

    # Método para carregar dados do objeto TurmaProfessor
    @staticmethod
    def get_instance(data):
        return {
            'id_turma': data.get('id_turma'),
            'id_professor': data.get('id_professor')
            # Adicione mais campos conforme necessário
        }

    # Método para validar a existência de um professor associado
    @staticmethod
    def validate_professor_exists(value):
        professor_id = value.get('id_professor')
        if not professor_id:
            raise ValidationError('ID do professor é obrigatório')

        if not Professor.query.get(professor_id):
            raise ValidationError(f'Professor com ID {professor_id} não encontrado')

    # Método para validar a existência de uma turma associada
    @staticmethod
    def validate_turma_exists(value):
        turma_id = value.get('id_turma')
        if not turma_id:
            raise ValidationError('ID da turma é obrigatório')

        if not Turma.query.get(turma_id):
            raise ValidationError(f'Turma com ID {turma_id} não encontrada')
