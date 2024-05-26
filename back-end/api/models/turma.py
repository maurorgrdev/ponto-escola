# turma.py

from api.config import db
from api.config import Base

class Turma(Base):
    __tablename__ = 'turma'

    # Definição do modelo da Turma
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # Relacionamento muitos para muitos com o modelo Materia
    materias = db.relationship('Materia', secondary='turma_materia', back_populates='turmas')

    # Relacionamento muitos para muitos com o modelo Professor
    professores = db.relationship('Professor', secondary='turma_professor', back_populates='turmas')

    planos = db.relationship('TurmaPlanoSemanalBimestre', back_populates='turma')