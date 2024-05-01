from app.models import TurmaProfessor, Professor, Turma
from app.schemas import TurmaProfessorSchema
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

class TurmaProfessorService:
    def __init__(self):
        self.turma_professor_schema = TurmaProfessorSchema()

    @handle_database_errors
    def get_all(self):
        turmas_professores = TurmaProfessor.query.all()
        return turmas_professores

    @handle_database_errors
    def get_by_id(self, id):
        turma_professor = TurmaProfessor.query.get(id)
        if not turma_professor:
            raise ValueError('Relação turma-professor não encontrada')
        return turma_professor

    @handle_database_errors
    def update(self, id, data):
        try:
            turma_professor_data = self.turma_professor_schema.load(data)
            
            turma_professor = TurmaProfessor.query.get(id)
            if not turma_professor:
                raise ValueError('Relação turma-professor não encontrada')
            
            # Atualiza os campos da relação turma-professor com os novos dados
            for key, value in turma_professor_data.items():
                setattr(turma_professor, key, value)
            
            # Salva as alterações no banco de dados
            db.session.commit()
            
            # Serializa a relação turma-professor atualizada
            turma_professor_serialized = self.turma_professor_schema.dump(turma_professor)
            
            # Retorna os dados da relação turma-professor atualizada
            return turma_professor_serialized, 200
        except ValidationError as err:
            return {'message': 'Erro de validação', 'errors': err.messages}, 400

    @handle_database_errors
    def delete(self, id):
        # Obtém a instância da relação turma-professor a ser deletada
        turma_professor = self.get_by_id(id)

        # Deleta a instância da relação turma-professor do banco de dados
        db.session.delete(turma_professor)
        
        # Confirma a transação no banco de dados para efetivar a remoção
        db.session.commit()

        # Retorna uma mensagem ou dados relevantes sobre a exclusão da relação turma-professor
        return {'message': f'Relação turma-professor com ID {id} deletada com sucesso'}

    @handle_database_errors
    def create(self, data):
        turma_professor_data = self.turma_professor_schema.load(data)
        nova_turma_professor = TurmaProfessor(**turma_professor_data)
        db.session.add(nova_turma_professor)
        db.session.commit()

        # Agora, retorne os dados da nova relação turma-professor como um dicionário serializável
        turma_professor_serialized = self.turma_professor_schema.dump(nova_turma_professor)
        return turma_professor_serialized, 201
    
    # @handle_database_errors
    def get_turmas_by_professor_id(self, id_professor):
        try:
            # Busca o professor pelo ID
            professor = Professor.query.get(id_professor)
            if not professor:
                raise ValueError('Professor não encontrado')

            return professor
        except SQLAlchemyError as e:
            # Captura exceções específicas do SQLAlchemy
            db.session.rollback()  # Desfaz qualquer transação pendente
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
        
    def get_professores_by_turma_id(self, id_turma):
        try:
            # Busca a turma pelo ID
            turma = Turma.query.get(id_turma)
            if not turma:
                raise ValueError('Turma não encontrada')

            # Retorna os professores associados a essa turma
            return turma
        except SQLAlchemyError as e:
            # Captura exceções específicas do SQLAlchemy
            db.session.rollback()  # Desfaz qualquer transação pendente
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))
