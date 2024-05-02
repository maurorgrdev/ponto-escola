from flask_restx import Namespace, fields
from app.schemas import TurmaSchema

turma_ns = Namespace('turmas', description='Operações relacionadas a turmas')

# Se houver modelos específicos para este namespace, você pode defini-los aqui
turma_model = turma_ns.model('Turma', {
    'id': fields.Integer(readOnly=True, description='Identificador único da turma'),
    # Defina outros campos da turma aqui
})

# Defina o esquema para serializar/desserializar objetos Turma
turma_schema = TurmaSchema()
