from flask_restx import Resource, fields, Namespace, Api
from flask import jsonify, request, Blueprint
from api.models import TurmaMateria  # Importe o modelo de TurmaMateria
from api.services import TurmaMateriaService  # Importe o serviço de TurmaMateria
from api.namespaces.turma_materia_namespace import  materia_turmas_schema, turma_materias_schema  # Importe o namespace e o schema de TurmaMateria

# Crie um Blueprint para o seu controller
turma_materia_bp = Blueprint('turma_materia_controller', __name__)

# Defina um Namespace para o seu controlador
turma_materia_ns = Namespace('turma_materia_controller', description='Operações relacionadas a alguma entidade')
@turma_materia_ns.route('/turmas-materias')
class TurmaMateriaList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()

    # @turma_materia_ns.doc(responses={201: 'Created', 400: 'Invalid Argument'})
    def post(self):
        data = request.json
        try:
            self.turma_materia_service.create(data)

            return {'message': 'Turma e matéria foram associadas com sucesso!'}
        except ValueError as e:
            return {'message': str(e)}, 400

@turma_materia_ns.route('/turmas/<int:id_turma>/materias')
class TurmaMateriaListByTurma(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()

    def get(self, id_turma):
        try:
            turma_materias = self.turma_materia_service.get_materias_by_turma_id(id_turma)
            serialized_data = turma_materias_schema.dump(turma_materias)
            return jsonify({'turma': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404


@turma_materia_ns.route('/materias/<int:id_materia>/turmas')
class MateriaTurmaListByMateria(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.turma_materia_service = TurmaMateriaService()

    def get(self, id_materia):
        try:
            materia_turmas = self.turma_materia_service.get_turmas_by_materia_id(id_materia)
            serialized_data = materia_turmas_schema.dump(materia_turmas)
            return jsonify({'materia': serialized_data})
        except ValueError as e:
            return {'message': str(e)}, 404
        
api = Api(turma_materia_bp)
api.add_namespace(turma_materia_ns)