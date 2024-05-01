from flask_restx import Resource, fields
from flask import jsonify, request
from app.models import TurmaMateria  # Importe o modelo de TurmaMateria
from app.services import TurmaMateriaService  # Importe o serviço de TurmaMateria
from app.namespaces import turma_materia_ns, turma_materia_schema, turma_materias_schema, materia_turmas_schema  # Importe o namespace e o schema de TurmaMateria

class TurmaMateriaController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()
        self.turma_materia_schema = turma_materia_schema

    def get(self, id):
        try:
            turma_materia = self.turma_materia_service.get_by_id(id)
            return jsonify(self.turma_materia_schema.dump(turma_materia))
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
    
    def put(self, id):
        data = request.json
        try:
            turma_materia = self.turma_materia_service.update(id, data)
            return {'message': f'TurmaMateria com ID {id} atualizada', 'turma_materia': turma_materia}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, id):
        try:
            self.turma_materia_service.delete(id)
            return jsonify({'message': f'TurmaMateria com ID {id} deletada com sucesso'})
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        
class TurmaMateriaList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()
        self.turma_materia_schema = turma_materia_schema

    def get(self):
        turmas_materias = self.turma_materia_service.get_all()
        return jsonify(self.turma_materia_schema.dump(turmas_materias, many=True))

    def post(self):
        data = request.json
        try:
            turma_materia = self.turma_materia_service.create(data)
            return {'message': 'Nova TurmaMateria criada', 'turma_materia': turma_materia}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

class TurmaMateriaListByTurma(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()

    def get(self, id_turma):
        try:
            turma_materias = self.turma_materia_service.get_materias_by_turma_id(id_turma)
            serialized_data = turma_materias_schema.dump(turma_materias)
            return jsonify({'turma': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404


class MateriaTurmaListByMateria(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()

    def get(self, id_materia):
        try:
            materia_turmas = self.turma_materia_service.get_turmas_by_materia_id(id_materia)
            serialized_data = materia_turmas_schema.dump(materia_turmas)
            return jsonify({'materia': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404