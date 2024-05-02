# professor_materia_controller.py

from flask_restx import Resource, fields
from flask import request
from app.services import ProfessorMateriaService, ProfessorService  # Importe o serviço de ProfessorMateria
from app.namespaces import materia_professores_schema, professor_materia_schema, professor_materias_schema  # Importe o namespace e o schema de ProfessorMateria
from flask import jsonify

from flask_restx import Resource, fields
from flask import request, jsonify
from app.services import ProfessorMateriaService, ProfessorService
from app.namespaces import professor_materia_ns, professor_materia_schema, professor_materias_schema

class ProfessorMateriaController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_materia_service = ProfessorMateriaService()
        self.professor_materia_schema = professor_materia_schema

    def get(self, id):
        try:
            professor_materia = self.professor_materia_service.get_by_id(id)
            return self.professor_materia_schema.dump(professor_materia)
        except ValueError as e:
            return {'message': str(e)}, 404
    
    def put(self, id):
        data = request.json
        try:
            professor_materia = self.professor_materia_service.update(id, data)
            return {'message': f'Relação ProfessorMateria com ID {id} atualizada', 'professor_materia': professor_materia}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, id):
        try:
            self.professor_materia_service.delete(id)
            return {'message': f'Relação ProfessorMateria com ID {id} deletada com sucesso'}
        except ValueError as e:
            return {'message': str(e)}, 400

class ProfessorMateriaList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_materia_service = ProfessorMateriaService()
        self.professor_materia_schema = professor_materia_schema
        self.professor_materias_schema = professor_materias_schema

    def get(self):
        professores_materias = self.professor_materia_service.get_all()
        return self.professor_materia_schema.dump(professores_materias, many=True)

    def post(self):
        data = request.json
        try:
            professor_materia = self.professor_materia_service.create(data)
            return {'message': 'Nova Relação ProfessorMateria criada', 'professor_materia': professor_materia}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

class ProfessorMateriaListByProfessor(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_materia_service = ProfessorMateriaService()

    def get(self, id_professor):
        try:
            professor = self.professor_materia_service.get_materias_by_professor_id(id_professor)
            serialized_data = professor_materias_schema.dump(professor)
            return jsonify({'professor': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404


class MateriaProfessorListByMateria(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_materia_service = ProfessorMateriaService()

    def get(self, id_materia):
        try:
            materia = self.professor_materia_service.get_professores_by_materia_id(id_materia)
            serialized_data = materia_professores_schema.dump(materia)
            return jsonify({'materia': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404
