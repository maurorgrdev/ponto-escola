from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from api.models import Materia  # Importe a classe Materia do arquivo correto
from api.services import MateriaService  # Importe o serviço correto para Materia
from api.namespaces.materia_namespace import materia_schema, materia_ns, materia_model  # Importe os namespaces e esquemas corretos para Materia

@materia_ns.route('/<int:id>')
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
    
    @materia_ns.expect(materia_model)
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
        
@materia_ns.route('/')
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

    @materia_ns.expect(materia_model)
    def post(self):
        data = request.json
        
        nova_materia = self.materia_service.create(data)
        
        return jsonify({
            'message'    : 'Matéria criada com sucesso!', 
            'materia'    : self.materia_schema.dump(nova_materia)
        })
