from app.models import ProfessorMateria, Professor, Materia
from app.schemas import ProfessorMateriaSchema
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

class ProfessorMateriaService:
    def __init__(self):
        self.professor_materia_schema = ProfessorMateriaSchema()

    @handle_database_errors
    def get_all(self):
        professores_materias = ProfessorMateria.query.all()
        return professores_materias

    @handle_database_errors
    def get_by_id(self, id):
        professor_materia = ProfessorMateria.query.get(id)
        if not professor_materia:
            raise ValueError('Relação professor-matéria não encontrada')
        return professor_materia

    @handle_database_errors
    def update(self, id, data):
        try:
            professor_materia_data = self.professor_materia_schema.load(data)
            
            professor_materia = ProfessorMateria.query.get(id)
            if not professor_materia:
                raise ValueError('Relação professor-matéria não encontrada')
            
            # Atualiza os campos da relação professor-matéria com os novos dados
            for key, value in professor_materia_data.items():
                setattr(professor_materia, key, value)
            
            # Salva as alterações no banco de dados
            db.session.commit()
            
            # Serializa a relação professor-matéria atualizada
            professor_materia_serialized = self.professor_materia_schema.dump(professor_materia)
            
            # Retorna os dados da relação professor-matéria atualizada
            return professor_materia_serialized, 200
        except ValidationError as err:
            return {'message': 'Erro de validação', 'errors': err.messages}, 400

    @handle_database_errors
    def delete(self, id):
        # Obtém a instância da relação professor-matéria a ser deletada
        professor_materia = self.get_by_id(id)

        # Deleta a instância da relação professor-matéria do banco de dados
        db.session.delete(professor_materia)
        
        # Confirma a transação no banco de dados para efetivar a remoção
        db.session.commit()

        # Retorna uma mensagem ou dados relevantes sobre a exclusão da relação professor-matéria
        return {'message': f'Relação professor-matéria com ID {id} deletada com sucesso'}

    @handle_database_errors
    def create(self, data):
        professor_materia_data = self.professor_materia_schema.load(data)
        nova_professor_materia = ProfessorMateria(**professor_materia_data)
        db.session.add(nova_professor_materia)
        db.session.commit()

        # Agora, retorne os dados da nova relação professor-matéria como um dicionário serializável
        professor_materia_serialized = self.professor_materia_schema.dump(nova_professor_materia)
        return professor_materia_serialized, 201

    # @handle_database_errors
    def get_materias_by_professor_id(self, id_professor):
        try:
            # Busca o professor pelo ID
            professor = Professor.query.get(id_professor)
            if not professor:
                raise ValueError('Professor não encontrado')

            #professor.materias = professor.materias
            # Retorna as matérias associadas ao professor
            return professor
        except SQLAlchemyError as e:
            # Captura exceções específicas do SQLAlchemy
            db.session.rollback()  # Desfaz qualquer transação pendente
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        
    def get_professores_by_materia_id(self, id_materia):
        try:
            # Busca a matéria pelo ID
            materia = Materia.query.get(id_materia)
            if not materia:
                raise ValueError('Matéria não encontrada')

            # Retorna os professores associados a essa matéria
            return materia
        except SQLAlchemyError as e:
            # Captura exceções específicas do SQLAlchemy
            db.session.rollback()  # Desfaz qualquer transação pendente
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))