from flask_restx import Namespace, fields
from api.schemas import TurmaProfessorSchema, TurmaProfessoresSchema, ProfessorTurmasSchema

turma_professor_ns = Namespace('turmas-professores', description='Operações relacionadas a turmas e professores')

turma_professor_model = turma_professor_ns.model('TurmaProfessor', {
    'id_turma': fields.Integer(required=True, description='ID da turma associada'),
    'id_professor': fields.Integer(required=True, description='ID do professor associado')
})

turma_professor_schema = TurmaProfessorSchema()

turma_professores_schema = TurmaProfessoresSchema()

professor_turmas_schema = ProfessorTurmasSchema()