from api.models import TurmaMateria, Turma, Materia
from api.schemas import TurmaMateriaSchema
from marshmallow import ValidationError
from api.config import db
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError



class TurmaMateriaService:
    def __init__(self):
        self.turma_materia_schema = TurmaMateriaSchema()

    def create(self, data):
        turma_materia_data = self.turma_materia_schema.load(data)
        
        nova_turma_materia = TurmaMateria(**turma_materia_data)
        
        db.session.add(nova_turma_materia)
        db.session.commit()

        return nova_turma_materia

    def get_materias_by_turma_id(self, id_turma):
        try:
            # Busca a turma pelo ID
            turma = Turma.query.get(id_turma)
            if not turma:
                raise ValueError('Turma não encontrada')

            return turma
        except SQLAlchemyError as e:
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        
    def get_turmas_by_materia_id(self, id_materia):
        try:
            # Busca a turma pelo ID
            materia = Materia.query.get(id_materia)
            if not materia:
                raise ValueError('Materia não encontrada')

            return materia
        except SQLAlchemyError as e:
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        