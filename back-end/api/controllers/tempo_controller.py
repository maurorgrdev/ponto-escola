from flask_restx import Resource
from flask import jsonify, request
from api.services import TempoService
from api.namespaces.tempo_namespace import tempo_ns, tempo_schema, tempo_model

@tempo_ns.route('/')
class TempoList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tempo_service = TempoService()
        self.tempo_schema = tempo_schema

    def get(self):
        tempos = self.tempo_service.get_all()
        return jsonify({
            'tempos': self.tempo_schema.dump(tempos, many=True)
        })

    @tempo_ns.expect(tempo_model)
    def post(self):
        data = request.json
        try:
            tempo = self.tempo_service.create(data)
            return jsonify({
                'message': 'Tempo criado com sucesso!', 
                'tempo': self.tempo_schema.dump(tempo)
            })
        except ValueError as e:
            return {'message': str(e)}, 400

@tempo_ns.route('/<int:id>')
class TempoController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tempo_service = TempoService()
        self.tempo_schema = tempo_schema

    def get(self, id):
        try:
            tempo = self.tempo_service.get_by_id(id)
            return jsonify({
                'tempo': self.tempo_schema.dump(tempo)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
    
    @tempo_ns.expect(tempo_model)
    def put(self, id):
        data = request.json
        try:
            tempo_atualizado = self.tempo_service.update(id, data)
            return jsonify({
                'message': f'Tempo com ID {id} atualizado', 
                'tempo': self.tempo_schema.dump(tempo_atualizado)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
    
    def delete(self, id):
        try:
            tempo_deletado = self.tempo_service.delete(id)
            return jsonify({
                'message': f'Tempo com ID {id} deletado com sucesso'
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
