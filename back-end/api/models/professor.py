# professor.py

from api.config import db
from api.config import Base

class Professor(Base):
    __tablename__ = 'professor'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # Relacionamento muitos para muitos com o modelo Materia
    materias = db.relationship('Materia', secondary='professor_materia', back_populates='professores')

    # Relacionamento muitos para muitos com o modelo Turma
    turmas = db.relationship('Turma', secondary='turma_professor', back_populates='professores')

    planos = db.relationship('TurmaPlanoSemanalBimestre', back_populates='professor')