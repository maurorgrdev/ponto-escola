from flask_restx import Namespace, fields
from api.schemas import MateriaSchema

materia_ns = Namespace('materias', description='Operações relacionadas a matérias')

materia_model = materia_ns.model('Materia', {
    'id': fields.Integer(readOnly=True, description='Identificador único da matéria')
})

materia_schema = MateriaSchema()
