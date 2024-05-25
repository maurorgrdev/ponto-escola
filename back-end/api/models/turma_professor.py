# turma_professor.py

from api.config import db
from api.config import Base

class TurmaProfessor(Base):
    
    id_turma = db.Column('id_turma', db.Integer, db.ForeignKey('turma.id'), primary_key=True, nullable=False)
    id_professor = db.Column('id_professor', db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
