from flask_restx import Namespace, fields
from app.schemas import TurmaMateriaSchema, TurmaMateriasSchema, MateriaTurmasSchema  # Importe o schema de TurmaMateria

turma_materia_ns = Namespace('turmas_materias', description='Operações relacionadas a turmas e matérias')

# Se houver modelos específicos para este namespace, você pode defini-los aqui
turma_materia_model = turma_materia_ns.model('TurmaMateria', {
    'id': fields.Integer(readOnly=True, description='Identificador único da relação turma-matéria'),
    'id_turma': fields.Integer(required=True, description='ID da turma associada'),
    'id_materia': fields.Integer(required=True, description='ID da matéria associada'),
    # Adicione outros campos conforme necessário
})

# Defina o esquema para serializar/desserializar objetos TurmaMateria
turma_materia_schema = TurmaMateriaSchema()

turma_materias_schema = TurmaMateriasSchema()

materia_turmas_schema = MateriaTurmasSchema()