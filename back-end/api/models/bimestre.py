from api.config import db, Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Bimestre(Base):
    __tablename__ = 'bimestre'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)

    planos = db.relationship('TurmaPlanoSemanalBimestre', back_populates='bimestre')