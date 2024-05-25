from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.frequencia_professor_turma_materia import FrequenciaProfessorTurmaMateria

class FrequenciaProfessorTurmaMateriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FrequenciaProfessorTurmaMateria
        load_instance = True
