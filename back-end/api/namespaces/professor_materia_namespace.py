from flask_restx import Namespace, fields
from api.schemas import ProfessorMateriaSchema, ProfessorMateriasSchema, MateriaProfessoresSchema # Importe o schema de ProfessorMateria

professor_materia_ns = Namespace('professores-materias', description='Operações relacionadas a professores e matérias')

professor_materia_model = professor_materia_ns.model('ProfessorMateria', {
    'id_professor': fields.Integer(required=True, description='ID do professor associado'),
    'id_materia': fields.Integer(required=True, description='ID da matéria associada'),
    # Adicione outros campos conforme necessário
})

professor_materia_schema = ProfessorMateriaSchema()

professor_materias_schema = ProfessorMateriasSchema()

materia_professores_schema = MateriaProfessoresSchema()


