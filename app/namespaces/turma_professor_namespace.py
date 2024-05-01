from flask_restx import Namespace, fields
from app.schemas import TurmaProfessorSchema, TurmaProfessoresSchema, ProfessorTurmasSchema

turma_professor_ns = Namespace('turmas_professores', description='Operações relacionadas a turmas e professores')

# Se houver modelos específicos para este namespace, você pode defini-los aqui
turma_professor_model = turma_professor_ns.model('TurmaProfessor', {
    'id': fields.Integer(readOnly=True, description='Identificador único da relação turma-professor'),
    'id_turma': fields.Integer(required=True, description='ID da turma associada'),
    'id_professor': fields.Integer(required=True, description='ID do professor associado'),
    # Adicione outros campos conforme necessário
})

# Defina o esquema para serializar/desserializar objetos TurmaProfessor
turma_professor_schema = TurmaProfessorSchema()

turma_professores_schema = TurmaProfessoresSchema()

professor_turmas_schema = ProfessorTurmasSchema()