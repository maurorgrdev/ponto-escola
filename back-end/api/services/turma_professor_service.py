from api.models import TurmaProfessor, Professor, Turma
from api.schemas import TurmaProfessorSchema
from marshmallow import ValidationError
from api.config import db
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError

class TurmaProfessorService:
    def __init__(self):
        self.turma_professor_schema = TurmaProfessorSchema()


    def create(self, data):
        turma_professor_data = self.turma_professor_schema.load(data)
        nova_turma_professor = TurmaProfessor(**turma_professor_data)

        db.session.add(nova_turma_professor)
        db.session.commit()

        return nova_turma_professor
    
    def get_turmas_by_professor_id(self, id_professor):
        try:
            professor = Professor.query.get(id_professor)
            if not professor:
                raise ValueError('Professor não encontrado')

            return professor
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        
    def get_professores_by_turma_id(self, id_turma):
        try:
            turma = Turma.query.get(id_turma)
            if not turma:
                raise ValueError('Turma não encontrada')

            return turma
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
