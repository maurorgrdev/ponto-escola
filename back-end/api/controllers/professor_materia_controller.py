# professor_materia_controller.py

from flask_restx import Resource
from flask import request
from api.services import ProfessorMateriaService
from api.namespaces.professor_materia_namespace import professor_materia_ns, professor_materia_model, \
    materia_professores_schema, professor_materia_schema, professor_materias_schema
from flask import jsonify

@professor_materia_ns.route('/')
class ProfessorMateriaList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_materia_service = ProfessorMateriaService()
        self.professor_materia_schema = professor_materia_schema
        self.professor_materias_schema = professor_materias_schema

    @professor_materia_ns.expect(professor_materia_model)
    def post(self):
        data = request.json
        try:
            professor_materia = self.professor_materia_service.create(data)
            return {'message': 'Nova Relação ProfessorMateria criada', 'professor_materia': professor_materia}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

@professor_materia_ns.route('/<int:id>/materias')
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

@professor_materia_ns.route('/<int:id>/professores')
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
