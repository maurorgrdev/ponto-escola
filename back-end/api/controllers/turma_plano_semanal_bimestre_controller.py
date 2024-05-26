# controllers/turma_plano_semanal_bimestre_controller.py

from flask_restx import Resource
from flask import jsonify, request
from api.services.turma_plano_semanal_bimestre_service import TurmaPlanoSemanalBimestreService
from api.namespaces.turma_plano_semanal_bimestre_namespace import turma_plano_ns, turma_plano_semanal_bimestre_schema, turma_plano_model

@turma_plano_ns.route('/')
class TurmaPlanoSemanalBimestreList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_plano_service = TurmaPlanoSemanalBimestreService()
        self.turma_plano_schema = turma_plano_semanal_bimestre_schema

    def get(self):
        planos = self.turma_plano_service.get_all()
        return jsonify({
            'planos': self.turma_plano_schema.dump(planos, many=True)
        })

    @turma_plano_ns.expect(turma_plano_model)
    def post(self):
        data = request.json
        try:
            plano = self.turma_plano_service.create(data)
            return jsonify({
                'message': 'Plano criado com sucesso!',
                'plano': self.turma_plano_schema.dump(plano)
            })
        except ValueError as e:
            return {'message': str(e)}, 400

@turma_plano_ns.route('/<int:id>')
class TurmaPlanoSemanalBimestreDetail(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_plano_service = TurmaPlanoSemanalBimestreService()
        self.turma_plano_schema = turma_plano_semanal_bimestre_schema

    def get(self, id):
        plano = self.turma_plano_service.get_by_id(id)
        if plano:
            return jsonify({
                'plano': self.turma_plano_schema.dump(plano)
            })
        return {'message': 'Plano não encontrado'}, 404

    @turma_plano_ns.expect(turma_plano_model)
    def put(self, id):
        data = request.json
        plano = self.turma_plano_service.update(id, data)
        if plano:
            return jsonify({
                'message': 'Plano atualizado com sucesso!',
                'plano': self.turma_plano_schema.dump(plano)
            })
        return {'message': 'Plano não encontrado'}, 404

    def delete(self, id):
        plano = self.turma_plano_service.delete(id)
        if plano:
            return jsonify({
                'message': 'Plano deletado com sucesso!',
                'plano': self.turma_plano_schema.dump(plano)
            })
        return {'message': 'Plano não encontrado'}, 404
