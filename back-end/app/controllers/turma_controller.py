# turma_controller.py

from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from app.models import Turma
from app.services import TurmaService
from app.namespaces import turma_ns, turma_model, turma_schema

class TurmaController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_service = TurmaService()
        self.turma_schema = turma_schema

    def get(self, id):
        try:
            turma = self.turma_service.get_by_id(id)
            
            return jsonify({
                'turma': turma_schema.dump(turma)
            })
        except ValueError as e:
            return jsonify({'message': str(e)})
    
    def put(self, id):
        data = request.json
        
        turma_atualizada = self.turma_service.update(id, data)

        return jsonify({
            'message': f'Turma com ID {id} atualizada', 
            'turma': turma_schema.dump(turma_atualizada)
        })
    
    def delete(self, id):
        try:
            turma_deletada = self.turma_service.delete(id)

            return jsonify({
                'message': f'Turma com ID {id} deletada com sucesso'
            })
        except ValueError as e:
            return jsonify({'message': str(e)})
        
class TurmaList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_service = TurmaService()
        self.turma_schema = turma_schema  # Defina o esquema da turma aqui

    def get(self):
        turmas = self.turma_service.get_all()

        return jsonify({
            'turmas': self.turma_schema.dump(turmas, many=True)
        })

    def post(self):
        data = request.json
        
        try:
            turma = self.turma_service.create(data)
            
            return jsonify({
                'message': 'Turma criada com sucesso!', 
                'turma': self.turma_schema.dump(turma)
            })
        except ValueError as e:
            return {'message': str(e)}



