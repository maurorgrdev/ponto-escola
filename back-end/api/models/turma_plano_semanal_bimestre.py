# turma_plano_semanal_bimestre.py

from api.config import db, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class TurmaPlanoSemanalBimestre(Base):
    __tablename__ = 'turma_plano_semanal_bimestre'

    id = Column(Integer, primary_key=True)
    turma_id = Column(Integer, ForeignKey('turma.id'), nullable=False)
    dia_semana = Column(String(15), nullable=False)
    bimestre_id = Column(Integer, ForeignKey('bimestre.id'), nullable=False)
    tempo_id = Column(Integer, ForeignKey('tempo.id'), nullable=False)
    materia_id = Column(Integer, ForeignKey('materia.id'), nullable=False)
    professor_id = Column(Integer, ForeignKey('professor.id'), nullable=False)

    frequencias = relationship('FrequenciaProfessorTurmaMateria', back_populates='plano')

    turma = relationship('Turma', back_populates='planos')
    bimestre = relationship('Bimestre', back_populates='planos')
    tempo = relationship('Tempo', back_populates='planos')
    materia = relationship('Materia', back_populates='planos')
    professor = relationship('Professor', back_populates='planos')