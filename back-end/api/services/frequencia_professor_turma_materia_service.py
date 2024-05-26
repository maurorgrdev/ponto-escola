from api.models import FrequenciaProfessorTurmaMateria, TurmaPlanoSemanalBimestre
from api.schemas.frequencia_professor_turma_materia_schema import FrequenciaProfessorTurmaMateriaSchema
from marshmallow import ValidationError
from api.config import db
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify
from werkzeug.utils import secure_filename

class FrequenciaProfessorTurmaMateriaService:
    def __init__(self):
        self.frequencia_schema = FrequenciaProfessorTurmaMateriaSchema()

    def registrar_presenca(self, data):
        try:
            frequencia_data = self.frequencia_schema.load(data)
            frequencia_data['presente'] = True
            nova_frequencia = FrequenciaProfessorTurmaMateria(**frequencia_data)
            db.session.add(nova_frequencia)
            db.session.commit()
            return nova_frequencia
        except ValidationError as err:
            return err.messages

    def registrar_ausencia(self, data):
        try:
            frequencia_data = self.frequencia_schema.load(data)
            frequencia_data['presente'] = False
            nova_frequencia = FrequenciaProfessorTurmaMateria(**frequencia_data)
            db.session.add(nova_frequencia)
            db.session.commit()
            return nova_frequencia
        except ValidationError as err:
            return err.messages

    def relatorio_frequencia_by_bimestre_professor(self, bimestre_id, professor_id):
        try:
            frequencias = FrequenciaProfessorTurmaMateria.query \
                .join(TurmaPlanoSemanalBimestre) \
                .filter(TurmaPlanoSemanalBimestre.bimestre_id == bimestre_id) \
                .filter(TurmaPlanoSemanalBimestre.professor_id == professor_id) \
                .all()
            return frequencias
        except Exception as e:
            return e

    def relatorio_frequencia_by_bimestre(self, bimestre_id):
        try:
            frequencias = FrequenciaProfessorTurmaMateria.query \
                .join(TurmaPlanoSemanalBimestre) \
                .filter(TurmaPlanoSemanalBimestre.bimestre_id == bimestre_id) \
                .all()
            return frequencias
        except Exception as e:
            return e

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