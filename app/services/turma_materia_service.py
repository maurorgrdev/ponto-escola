from app.models import TurmaMateria, Turma, Materia
from app.schemas import TurmaMateriaSchema
from marshmallow import ValidationError
from app.config import db
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError

def handle_database_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Aqui você pode adicionar o tratamento de exceção para erros de servidor de banco de dados
            return {'message': 'Erro de servidor de banco de dados'}, 500
    return wrapper

class TurmaMateriaService:
    def __init__(self):
        self.turma_materia_schema = TurmaMateriaSchema()

    @handle_database_errors
    def get_all(self):
        turmas_materias = TurmaMateria.query.all()
        return turmas_materias

    @handle_database_errors
    def get_by_id(self, id):
        turma_materia = TurmaMateria.query.get(id)
        if not turma_materia:
            raise ValueError('Relação turma-matéria não encontrada')
        return turma_materia

    @handle_database_errors
    def update(self, id, data):
        try:
            turma_materia_data = self.turma_materia_schema.load(data)
            
            turma_materia = TurmaMateria.query.get(id)
            if not turma_materia:
                raise ValueError('Relação turma-matéria não encontrada')
            
            # Atualiza os campos da relação turma-matéria com os novos dados
            for key, value in turma_materia_data.items():
                setattr(turma_materia, key, value)
            
            # Salva as alterações no banco de dados
            db.session.commit()
            
            # Serializa a relação turma-matéria atualizada
            turma_materia_serialized = self.turma_materia_schema.dump(turma_materia)
            
            # Retorna os dados da relação turma-matéria atualizada
            return turma_materia_serialized, 200
        except ValidationError as err:
            return {'message': 'Erro de validação', 'errors': err.messages}, 400

    @handle_database_errors
    def delete(self, id):
        # Obtém a instância da relação turma-matéria a ser deletada
        turma_materia = self.get_turma_materia_by_id(id)

        # Deleta a instância da relação turma-matéria do banco de dados
        db.session.delete(turma_materia)
        
        # Confirma a transação no banco de dados para efetivar a remoção
        db.session.commit()

        # Retorna uma mensagem ou dados relevantes sobre a exclusão da relação turma-matéria
        return {'message': f'Relação turma-matéria com ID {id} deletada com sucesso'}

    @handle_database_errors
    def create(self, data):
        turma_materia_data = self.turma_materia_schema.load(data)
        nova_turma_materia = TurmaMateria(**turma_materia_data)
        db.session.add(nova_turma_materia)
        db.session.commit()

        # Agora, retorne os dados da nova relação turma-matéria como um dicionário serializável
        turma_materia_serialized = self.turma_materia_schema.dump(nova_turma_materia)
        return turma_materia_serialized, 201

     # @handle_database_errors
    def get_materias_by_turma_id(self, id_turma):
        try:
            # Busca a turma pelo ID
            turma = Turma.query.get(id_turma)
            if not turma:
                raise ValueError('Turma não encontrada')

            return turma
        except SQLAlchemyError as e:
            # Captura exceções específicas do SQLAlchemy
            db.session.rollback()  # Desfaz qualquer transação pendente
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        
    def get_turmas_by_materia_id(self, id_materia):
        try:
            # Busca a turma pelo ID
            materia = Materia.query.get(id_materia)
            if not materia:
                raise ValueError('Materia não encontrada')

            return materia
        except SQLAlchemyError as e:
            # Captura exceções específicas do SQLAlchemy
            db.session.rollback()  # Desfaz qualquer transação pendente
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        