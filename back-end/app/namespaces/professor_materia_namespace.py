from flask_restx import Namespace, fields
from app.schemas import ProfessorMateriaSchema, ProfessorMateriasSchema, MateriaProfessoresSchema # Importe o schema de ProfessorMateria

professor_materia_ns = Namespace('professores_materias', description='Operações relacionadas a professores e matérias')

# Se houver modelos específicos para este namespace, você pode defini-los aqui
professor_materia_model = professor_materia_ns.model('ProfessorMateria', {
    'id': fields.Integer(readOnly=True, description='Identificador único da relação professor-matéria'),
    'id_professor': fields.Integer(required=True, description='ID do professor associado'),
    'id_materia': fields.Integer(required=True, description='ID da matéria associada'),
    # Adicione outros campos conforme necessário
})

# Defina o esquema para serializar/desserializar objetos ProfessorMateria
professor_materia_schema = ProfessorMateriaSchema()

professor_materias_schema = ProfessorMateriasSchema()

materia_professores_schema = MateriaProfessoresSchema()


