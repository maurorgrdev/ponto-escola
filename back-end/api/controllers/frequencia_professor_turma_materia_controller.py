from flask_restx import Resource
from flask import jsonify, request
from api.services import FrequenciaService
from api.namespaces.frequencia_professor_turma_materia_namespace import frequencia_ns, frequencia_schema, frequencia_model

@frequencia_ns.route('/presenca')
class RegistrarPresenca(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frequencia_service = FrequenciaService()
        self.frequencia_schema = frequencia_schema

    @frequencia_ns.expect(frequencia_model)
    def post(self):
        data = request.json
        try:
            frequencia = self.frequencia_service.registrar_presenca(data)
            return jsonify({
                'message': 'Presença registrada com sucesso!', 
                'frequencia': self.frequencia_schema.dump(frequencia)
            })
        except ValueError as e:
            return {'message': str(e)}, 400

@frequencia_ns.route('/ausencia')
class RegistrarAusencia(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frequencia_service = FrequenciaService()
        self.frequencia_schema = frequencia_schema

    @frequencia_ns.expect(frequencia_model)
    def post(self):
        data = request.json
        try:
            frequencia = self.frequencia_service.registrar_ausencia(data)
            return jsonify({
                'message': 'Ausência registrada com sucesso!', 
                'frequencia': self.frequencia_schema.dump(frequencia)
            })
        except ValueError as e:
            return {'message': str(e)}, 400

@frequencia_ns.route('/relatorio/bimestre/<int:bimestre_id>/professor/<int:professor_id>')
class RelatorioFrequenciaByBimestreProfessor(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frequencia_service = FrequenciaService()
        self.frequencia_schema = frequencia_schema

    def get(self, bimestre_id, professor_id):
        try:
            frequencias = self.frequencia_service.relatorio_frequencia_by_bimestre_professor(bimestre_id, professor_id)
            return jsonify({
                'frequencias': self.frequencia_schema.dump(frequencias, many=True)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404

@frequencia_ns.route('/relatorio/bimestre/<int:bimestre_id>')
class RelatorioFrequenciaByBimestre(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frequencia_service = FrequenciaService()
        self.frequencia_schema = frequencia_schema

    def get(self, bimestre_id):
        try:
            frequencias = self.frequencia_service.relatorio_frequencia_by_bimestre(bimestre_id)
            return jsonify({
                'frequencias': self.frequencia_schema.dump(frequencias, many=True)
            })
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
