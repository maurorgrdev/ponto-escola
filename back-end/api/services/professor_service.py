# professor_service.py

from api.models import Professor  # Importe o modelo de Professor
from api.schemas import ProfessorSchema  # Importe o schema de Professor
from marshmallow import ValidationError
from api.config import db
from functools import wraps
from api.models import FrequenciaProfessorTurmaMateria, TurmaPlanoSemanalBimestre

class ProfessorService:
    def __init__(self):
        self.professor_schema = ProfessorSchema()

    def get_all(self):
        professores = Professor.query.all()

        return professores

    def get_by_id(self, id):
        professor = Professor.query.get(id)

        if not professor:
            raise ValueError('Professor não encontrado')
        
        return professor

    def update(self, id, data):
        try:
            professor_data = self.professor_schema.load(data)
            
            professor = Professor.query.get(id)
            if not professor:
                raise ValueError('Professor não encontrado')
            
            for key, value in professor_data.items():
                setattr(professor, key, value)
            
            db.session.commit()
            
            return professor
        except ValidationError as err:
            return err.messages

    def delete(self, id):
        professor = self.get_by_id(id)

        db.session.delete(professor)
        db.session.commit()

        return professor

    def create(self, data):
        professor_data = self.professor_schema.load(data)
        novo_professor = Professor(**professor_data)
        db.session.add(novo_professor)
        db.session.commit()

        return novo_professor

    def get_professor_faltas(self):
        relatorio = []
        professores = Professor.query.all()
        for professor in professores:
            professor_data = self.professor_schema.dump(professor)
            professor_data['materias'] = []
            planos = TurmaPlanoSemanalBimestre.query.filter_by(professor_id=professor.id).all()
            for plano in planos:
                faltas = FrequenciaProfessorTurmaMateria.query.filter_by(plano_id=plano.id, presente=False).count()
                materia_turma = {
                    'materia_id': plano.materia_id,
                    'turma_id': plano.turma_id,
                    'faltas': faltas
                }
                professor_data['materias'].append(materia_turma)
            relatorio.append(professor_data)
        return relatorio