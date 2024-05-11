from flask_restx import Namespace, fields
from api.schemas import ProfessorSchema

professor_ns = Namespace('professores', description='Operações relacionadas a professor')

professor_model = professor_ns.model('Professor', {
    'id': fields.Integer(readOnly=True, description='Identificador único do professor'),
})

professor_schema = ProfessorSchema()
