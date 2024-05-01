from app.models import Materia
from app.schemas import MateriaSchema
from marshmallow import ValidationError
from flask import jsonify
from app.config import db

class MateriaFacade:
    def __init__(self):
        self.materia_schema = MateriaSchema()

    def serialize_data(self, data):
        try:
            serialized_data = [self.materia_schema.dump(item) for item in data]
            return jsonify(serialized_data)
        except ValidationError as e:
            return {'message': 'Erro de validação', 'errors': e.messages}, 400
        except Exception as e:
            return {'message': 'Erro ao serializar dados'}, 500