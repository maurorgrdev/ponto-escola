from api.models import Bimestre
from api.schemas import BimestreSchema
from marshmallow import ValidationError
from api.config import db


class BimestreService:
    def __init__(self):
        self.bimestre_schema = BimestreSchema()

    def get_all(self):
        try:
            bimestres = Bimestre.query.all()
            return bimestres
        except Exception as e:
            return e

    def get_by_id(self, id):
        bimestre = Bimestre.query.get(id)
        if not bimestre:
            raise ValueError('Bimestre não encontrado')
        return bimestre

    def update(self, id, data):
        try:
            bimestre_data = self.bimestre_schema.load(data)
            bimestre = Bimestre.query.get(id)
            if not bimestre:
                raise ValueError('Bimestre não encontrado')

            for key, value in bimestre_data.items():
                setattr(bimestre, key, value)

            db.session.commit()
            return bimestre
        except ValidationError as err:
            return err.messages

    def delete(self, id):
        bimestre = self.get_by_id(id)
        if not bimestre:
            raise ValueError('Bimestre não encontrado')

        db.session.delete(bimestre)
        db.session.commit()
        return bimestre

    def create(self, data):
        try:
            bimestre_data = self.bimestre_schema.load(data)
            novo_bimestre = Bimestre(**bimestre_data)
            db.session.add(novo_bimestre)
            db.session.commit()
            return novo_bimestre
        except ValidationError as err:
            return err.messages
