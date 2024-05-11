from api.config import db
from sqlalchemy import Column, Integer, ForeignKey, String, Date, Boolean
from sqlalchemy.orm import relationship

class PresencaProfessorTurmaMateria(db.Model):
    __tablename__ = 'presenca_professor_turma_materia'

    id = Column(Integer, primary_key=True)
    professor_id = Column(Integer, ForeignKey('professor.id'))
    data = Column(Date)
    materia_id = Column(Integer, ForeignKey('materia.id'))
    turma_id = Column(Integer, ForeignKey('turma.id'))
    presente = Column(Boolean, nullable=False)

    professor = relationship("Professor")
    materia = relationship("Materia")
    turma = relationship("Turma")
