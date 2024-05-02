from flask_restx import Resource, fields
from flask import jsonify, request
from app.models import TurmaProfessor  # Importe o modelo de TurmaProfessor
from app.services import TurmaProfessorService  # Importe o serviço de TurmaProfessor
from app.namespaces import turma_professor_schema, turma_professores_schema, professor_turmas_schema  # Importe o namespace e o schema de TurmaProfessor

class TurmaProfessorController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_professor_service = TurmaProfessorService()
        self.turma_professor_schema = turma_professor_schema

    def get(self):
        turmas_professores = self.turma_professor_service.get_all()
        return jsonify(self.turma_professor_schema.dump(turmas_professores, many=True))

    def get(self, id):
        try:
            turma_professor = self.turma_professor_service.get_by_id(id)
            return jsonify(self.turma_professor_schema.dump(turma_professor))
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
    
    def put(self, id):
        data = request.json
        try:
            turma_professor = self.turma_professor_service.update(id, data)
            return {'message': f'TurmaProfessor com ID {id} atualizado', 'turma_professor': turma_professor}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, id):
        try:
            self.turma_professor_service.delete(id)
            return jsonify({'message': f'TurmaProfessor com ID {id} deletado com sucesso'})
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        
class TurmaProfessorList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_professor_service = TurmaProfessorService()
        self.turma_professor_schema = turma_professor_schema

    def get(self):
        turmas_professores = self.turma_professor_service.get_all()
        return jsonify(self.turma_professor_schema.dump(turmas_professores, many=True))

    def post(self):
        data = request.json
        try:
            turma_professor = self.turma_professor_service.create(data)
            return {'message': 'Nova TurmaProfessor criada', 'turma_professor': turma_professor}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

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