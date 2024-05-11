# turma_service.py

from api.models import Turma, PresencaProfessorTurmaMateria
from api.schemas import TurmaSchema
from marshmallow import ValidationError
from api.config import db
from flask import jsonify
from functools import wraps


class TurmaService:
    def __init__(self):
        self.turma_schema = TurmaSchema()

    def get_all(self):
        try:
            turmas = Turma.query.all()
            x = PresencaProfessorTurmaMateria.query.all()
        
            return turmas
        except Exception as e:
            return e

    def get_by_id(self, id):
        turma = Turma.query.get(id)
        
        if not turma:
            raise ValueError('Turma não encontrada')
        
        return turma

    def update(self, id, data):
        try:
            turma_data = self.turma_schema.load(data)
            
            turma = Turma.query.get(id)
            if not turma:
                raise ValueError('Turma não encontrada')
            
            for key, value in turma_data.items():
                setattr(turma, key, value)
            
            db.session.commit()
            
            return turma
        except ValidationError as err:
            return err.messages

    def delete(self, id):
        turma = self.get_turma_by_id(id)

        db.session.delete(turma)
        db.session.commit()

        return turma

    def create(self, data):
        turma_data = self.turma_schema.load(data)
        nova_turma = Turma(**turma_data)
        db.session.add(nova_turma)
        db.session.commit()

        return nova_turma
