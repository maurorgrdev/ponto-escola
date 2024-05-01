from app.config import db
from app.config import Base

class TurmaMateria(Base):

    id_turma = db.Column('id_turma', db.Integer, db.ForeignKey('turma.id'), primary_key=True, nullable=False)
    id_materia = db.Column('id_materia', db.Integer, db.ForeignKey('materia.id'), primary_key=True, nullable=False)
