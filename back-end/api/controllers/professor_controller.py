# professor_controller.py

from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from api.services import ProfessorService
from api.namespaces.professor_namespace import professor_ns, professor_schema, professor_model

@professor_ns.route('/')
class ProfessorController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_service = ProfessorService()
        self.professor_schema = professor_schema

    def get(self, id):
        try:
            professor = self.professor_service.get_by_id(id)

            return jsonify({
                'professor': self.professor_schema.dump(professor)
            })
        except ValueError as e:
            return jsonify({
                'message': str(e)
            }), 
    
    @professor_ns.expect(professor_model)
    def put(self, id):
        data = request.json

        try:
            professor = self.professor_service.update(id, data)

            return jsonify({
                'message': f'Professor com ID {id} atualizado', 
                'professor': self.professor_schema.dump(professor)
            })
        except ValueError as e:
            return jsonify({
                'message': str(e)
            })

    def delete(self, id):
        try:
            professor = self.professor_service.delete(id)

            return jsonify({
                'message': f'Professor com ID {id} deletado com sucesso'
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        
@professor_ns.route('/<int:id>')
class ProfessorList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.professor_service = ProfessorService()
        self.professor_schema = professor_schema

    def get(self):
        professores = self.professor_service.get_all()

        return jsonify({
            'professores': self.professor_schema.dump(professores, many=True)
        })

    @professor_ns.expect(professor_model)
    def post(self):
        data = request.json

        try:
            professor = self.professor_service.create(data)

            return jsonify({
                'message': 'Novo professor criado', 
                'professor': self.professor_schema.dump(professor)
            })
        except ValueError as e:
            return {'message': str(e)}
