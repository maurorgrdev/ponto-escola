# professor_materia.py

from app.config import db
from app.config import Base

class ProfessorMateria(Base):

    id_professor = db.Column('id_professor', db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
    id_materia = db.Column('id_materia', db.Integer, db.ForeignKey('materia.id'), primary_key=True, nullable=False)