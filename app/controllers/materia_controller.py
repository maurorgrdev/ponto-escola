from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from app.models import Materia  # Importe a classe Materia do arquivo correto
from app.services import MateriaService  # Importe o serviço correto para Materia
from app.namespaces import materia_schema  # Importe os namespaces e esquemas corretos para Materia

class MateriaController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.materia_service = MateriaService()
        self.materia_schema = materia_schema

    def get(self, id):
        try:
            materia = self.materia_service.get_by_id(id)

            return jsonify({
                'materia': materia_schema.dump(materia)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
    
    def put(self, id):
        data = request.json

        materia_atualizada = self.materia_service.update(id, data)

        return jsonify({
            'message'    : f'Matéria com ID {id} atualizada', 
            'materia'    : materia_schema.dump(materia_atualizada)
        })

    def delete(self, id):
        try:
            materia_deletada = self.materia_service.delete(id)

            return jsonify({
                'message'     : f'Matéria com ID {id} deletada com sucesso'
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        
class MateriaList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.materia_service = MateriaService()
        self.materia_schema = materia_schema  # Defina o esquema da materia aqui

    def get(self):
        materias = self.materia_service.get_all()
        
        return jsonify({
            'materias'   : self.materia_schema.dump(materias, many=True)
        })

    def post(self):
        data = request.json
        
        nova_materia = self.materia_service.create(data)
        
        return {
            'message'    : 'Matéria criada com sucesso!', 
            'materia'    : self.materia_schema.dump(nova_materia)
        }
