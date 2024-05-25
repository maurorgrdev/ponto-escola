from api.config import db, Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship

class FrequenciaProfessorTurmaMateria(Base):
    __tablename__ = 'frequencia_professor_turma_materia'

    id = Column(Integer, primary_key=True)
    plano_id = Column(Integer, ForeignKey('turma_plano_semanal_bimestre.id'), nullable=False)
    data = Column(Date, nullable=False)
    presente = Column(Boolean, nullable=False)
