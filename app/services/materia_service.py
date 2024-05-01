from app.models import Materia
from app.schemas import MateriaSchema
from app.facades import MateriaFacade
from marshmallow import ValidationError
from app.config import db
from functools import wraps
from flask import jsonify

class MateriaService:
    def __init__(self):
        self.materia_schema = MateriaSchema()

    def get_all(self):
        try:
            materias = Materia.query.all()

            return materias
        except Exception as e:
            return e

    def get_by_id(self, id):
        materia = Materia.query.get(id)

        if not materia:
            raise ValueError('Matéria não encontrada')
        
        return materia

    def update(self, id, data):
        materia_data = self.materia_schema.load(data)
        
        materia = Materia.query.get(id)
        if not materia:
            raise ValueError('Matéria não encontrada')
        
        for key, value in materia_data.items():
            setattr(materia, key, value)
        
        db.session.commit()
        
        return materia

    def delete(self, id):
        materia = Materia.query.get(id)

        db.session.delete(materia)
        db.session.commit()

        return materia

    def create(self, data):
        materia_data = self.materia_schema.load(data)
        nova_materia = Materia(**materia_data)
        db.session.add(nova_materia)
        db.session.commit()

        return nova_materia
