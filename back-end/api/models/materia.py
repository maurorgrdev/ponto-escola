# materia.py

from api.config import db
from api.config import Base

class Materia(Base):
    __tablename__ = 'materia'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # Relacionamento muitos para muitos com o modelo Professor
    professores = db.relationship('Professor', secondary='professor_materia', back_populates='materias')

    # Relacionamento muitos para muitos com o modelo Turma
    turmas = db.relationship('Turma', secondary='turma_materia', back_populates='materias')

    planos = db.relationship('TurmaPlanoSemanalBimestre', back_populates='materia')