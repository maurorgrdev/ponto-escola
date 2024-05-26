from flask_restx import Resource
from flask import jsonify, request
from api.services import BimestreService
from api.namespaces.bimestre_namespace import bimestre_ns, bimestre_schema, bimestre_model

@bimestre_ns.route('/')
class BimestreList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bimestre_service = BimestreService()
        self.bimestre_schema = bimestre_schema

    def get(self):
        bimestres = self.bimestre_service.get_all()
        
        return jsonify({
            'bimestres': self.bimestre_schema.dump(bimestres, many=True)
        })

    @bimestre_ns.expect(bimestre_model)
    def post(self):
        data = request.json
        
        try:
            bimestre = self.bimestre_service.create(data)
            
            return jsonify({
                'message': 'Bimestre criado com sucesso!', 
                'bimestre': self.bimestre_schema.dump(bimestre)
            })
        except ValueError as e:
            return {'message': str(e)}, 400

@bimestre_ns.route('/<int:id>')
class BimestreController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bimestre_service = BimestreService()
        self.bimestre_schema = bimestre_schema

    def get(self, id):
        try:
            bimestre = self.bimestre_service.get_by_id(id)
            
            return jsonify({
                'bimestre': self.bimestre_schema.dump(bimestre)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
    
    @bimestre_ns.expect(bimestre_model)
    def put(self, id):
        data = request.json
        
        try:
            bimestre_atualizado = self.bimestre_service.update(id, data)
            
            return jsonify({
                'message': f'Bimestre com ID {id} atualizado', 
                'bimestre': self.bimestre_schema.dump(bimestre_atualizado)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
    
    def delete(self, id):
        try:
            bimestre_deletado = self.bimestre_service.delete(id)
            
            return jsonify({
                'message': f'Bimestre com ID {id} deletado com sucesso'
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
