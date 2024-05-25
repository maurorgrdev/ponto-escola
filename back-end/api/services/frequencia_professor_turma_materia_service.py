from api.models.frequencia_professor_turma_materia import FrequenciaProfessorTurmaMateria
from api.schemas.frequencia_professor_turma_materia_schema import FrequenciaProfessorTurmaMateriaSchema
from marshmallow import ValidationError
from api.config import db
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify
from werkzeug.utils import secure_filename

class FrequenciaProfessorTurmaMateriaService:
    def __init__(self):
        self.frequencia_professor_schema = FrequenciaProfessorTurmaMateriaSchema()

    def create(self, data):
        try:
            frequencia_professor_data = self.frequencia_professor_schema.load(data)
            nova_frequencia_professor = FrequenciaProfessorTurmaMateria(**frequencia_professor_data)

            db.session.add(nova_frequencia_professor)
            db.session.commit()

            return nova_frequencia_professor
        except ValidationError as e:
            raise ValueError('Erro de validação: {}'.format(e.messages))
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))

    def get_frequencia_by_professor_id_and_date(self, professor_id, data):
        try:
            frequencia_professor = FrequenciaProfessorTurmaMateria.query.filter_by(professor_id=professor_id, data=data).first()
            if not frequencia_professor:
                raise ValueError('Presença do professor não encontrada')

            return frequencia_professor
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError('Erro no servidor de banco de dados: {}'.format(str(e)))

    def upload_arquivo(self):
        try:
            # Verificar se foi enviado algum arquivo
            if 'file' not in request.files:
                return jsonify({'error': 'Nenhum arquivo enviado'}), 400
            
            file = request.files['file']
            
            # Verificar se o arquivo tem um nome
            if file.filename == '':
                return jsonify({'error': 'Nome de arquivo inválido'}), 400
            
            # Salvar o arquivo no diretório de uploads
            filename = secure_filename(file.filename)
            file.save('/Users/mauroroger/Desktop/' + filename)

            return jsonify({'message': 'Arquivo salvo com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500