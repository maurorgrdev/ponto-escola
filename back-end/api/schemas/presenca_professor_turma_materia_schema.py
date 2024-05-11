from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.presenca_professor_turma_materia import PresencaProfessorTurmaMateria

class PresencaProfessorTurmaMateriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PresencaProfessorTurmaMateria
        load_instance = True
