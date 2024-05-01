from flask_restx import Namespace, fields
from app.schemas import MateriaSchema  # Importe o esquema correto para Materia

materia_ns = Namespace('materias', description='Operações relacionadas a matérias')

# Se houver modelos específicos para este namespace, você pode defini-los aqui
materia_model = materia_ns.model('Materia', {
    'id': fields.Integer(readOnly=True, description='Identificador único da matéria'),
    # Defina outros campos da matéria aqui
})

# Defina o esquema para serializar/desserializar objetos Materia
materia_schema = MateriaSchema()
