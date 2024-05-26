# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from api.models.frequencia_professor_turma_materia import FrequenciaProfessorTurmaMateria

# class FrequenciaProfessorTurmaMateriaSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = FrequenciaProfessorTurmaMateria
#         load_instance = True

class FrequenciaProfessorTurmaMateriaSchema(Schema):
    id = fields.Int(dump_only=True)
    plano_id = fields.Int(required=True)
    data = fields.Date(required=True)
    presente = fields.Boolean()
