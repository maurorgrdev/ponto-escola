from marshmallow import Schema, fields, validate, ValidationError
from .materia_schema import MateriaSchema
from .professor_schema import ProfessorSchema
from app.models import Materia, Professor
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class MateriaProfessoresSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Materia
        load_instance = True
    
    professores = fields.Nested('ProfessorSchema', many=True)  

class ProfessorMateriasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Professor
        load_instance = True
    
    materias = fields.Nested('MateriaSchema', many=True)  

class ProfessorMateriaSchema(Schema):
    id_professor = fields.Integer(required=True)
    id_materia = fields.Integer(required=True)

    # Método para validar a existência de uma matéria associada
    @staticmethod
    def validate_materia_exists(value):
        materia_id = value.get('id_materia')
        if not materia_id:
            raise ValidationError('ID da matéria é obrigatório')

        if not Materia.query.get(materia_id):
            raise ValidationError(f'Matéria com ID {materia_id} não encontrada')

    # Método para validar a existência de um professor associado
    @staticmethod
    def validate_professor_exists(value):
        professor_id = value.get('id_professor')
        if not professor_id:
            raise ValidationError('ID do professor é obrigatório')

        if not Professor.query.get(professor_id):
            raise ValidationError(f'Professor com ID {professor_id} não encontrado')
