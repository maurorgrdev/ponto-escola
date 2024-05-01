# professor_controller.py

from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from app.models import Professor  # Importe o modelo de Professor
from app.services import ProfessorService  # Importe o serviço de Professor
from app.namespaces import professor_ns, professor_schema  # Importe o namespace e o schema de Professor

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
