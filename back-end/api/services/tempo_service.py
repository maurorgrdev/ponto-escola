from api.models import Tempo
from api.schemas import TempoSchema
from marshmallow import ValidationError
from api.config import db

class TempoService:
    def __init__(self):
        self.tempo_schema = TempoSchema()

    def get_all(self):
        try:
            tempos = Tempo.query.all()
            return tempos
        except Exception as e:
            return e

    def get_by_id(self, id):
        tempo = Tempo.query.get(id)
        if not tempo:
            raise ValueError('Tempo não encontrado')
        return tempo

    def update(self, id, data):
        try:
            tempo_data = self.tempo_schema.load(data)
            tempo = Tempo.query.get(id)
            if not tempo:
                raise ValueError('Tempo não encontrado')

            for key, value in tempo_data.items():
                setattr(tempo, key, value)

            db.session.commit()
            return tempo
        except ValidationError as err:
            return err.messages

    def delete(self, id):
        tempo = self.get_by_id(id)
        if not tempo:
            raise ValueError('Tempo não encontrado')

        db.session.delete(tempo)
        db.session.commit()
        return tempo

    def create(self, data):
        try:
            tempo_data = self.tempo_schema.load(data)
            novo_tempo = Tempo(**tempo_data)
            db.session.add(novo_tempo)
            db.session.commit()
            return novo_tempo
        except ValidationError as err:
            return err.messages
