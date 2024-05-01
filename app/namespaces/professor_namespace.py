from flask_restx import Namespace, fields
from app.schemas import ProfessorSchema

professor_ns = Namespace('professores', description='Operações relacionadas a professores')

# Se houver modelos específicos para este namespace, você pode defini-los aqui
professor_model = professor_ns.model('Professor', {
    'id': fields.Integer(readOnly=True, description='Identificador único do professor'),
    # Defina outros campos da turma aqui
})

# Defina o esquema para serializar/desserializar objetos Professor
professor_schema = ProfessorSchema()
