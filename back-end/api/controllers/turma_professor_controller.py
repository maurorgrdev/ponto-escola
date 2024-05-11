from flask_restx import Resource
from flask import jsonify, request
from api.services import TurmaProfessorService
from api.namespaces.turma_professor_namespace import turma_professor_ns, turma_professor_model, \
    turma_professor_schema, turma_professores_schema, professor_turmas_schema

@turma_professor_ns.route('/')
class TurmaProfessorList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_professor_service = TurmaProfessorService()
        self.turma_professor_schema = turma_professor_schema

    @turma_professor_ns.expect(turma_professor_model)
    def post(self):
        data = request.json
        try:
            turma_professor = self.turma_professor_service.create(data)
            
            return {'message': 'Turma e matéria foram associadas com sucesso!'}
        except ValueError as e:
            return {'message': str(e)}, 400

@turma_professor_ns.route('/<int:id_turma>/profesores')
class TurmaProfessorListByTurma(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_professor_service = TurmaProfessorService()

    def get(self, id_turma):
        try:
            turma_professores = self.turma_professor_service.get_professores_by_turma_id(id_turma)
            
            serialized_data = turma_professores_schema.dump(turma_professores)
            
            return jsonify({'turma': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404

@turma_professor_ns.route('/<int:id_turma>/turmas')
class ProfessorTurmaListByProfessor(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_professor_service = TurmaProfessorService()

    def get(self, id_professor):
        try:
            profesor_turmas = self.turma_professor_service.get_turmas_by_professor_id(id_professor)
            
            serialized_data = professor_turmas_schema.dump(profesor_turmas)

            return jsonify({'professor': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404