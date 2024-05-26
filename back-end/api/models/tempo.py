from api.config import db, Base
from sqlalchemy import Column, Integer, Time, String, Date, Boolean
from sqlalchemy.orm import relationship

class Tempo(Base):
    __tablename__ = 'tempo'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)
    horario_inicio = Column(Time, nullable=False)
    horario_fim = Column(Time, nullable=False)

    planos = db.relationship('TurmaPlanoSemanalBimestre', back_populates='tempo')