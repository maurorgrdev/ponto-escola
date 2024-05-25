# arquivo_anexo_frequencia.py

from api.config import db
from sqlalchemy import Column, Integer, ForeignKey, String, Date, Boolean
from sqlalchemy.orm import relationship

class ArquivoAnexoFrequencia(db.Model):
    __tablename__ = 'arquivo'
    
    id = Column(Integer, primary_key=True)
    professor_frequencia_id = Column(Integer, ForeignKey('frequencia_professor_turma_materia.id'))
    caminho = Column(String) 
    tipo_arquivo = Column(String)
    nome_arquivo = Column(String)
    apelido = Column(String)
    tamanho = Column(Integer)
    
    presenca = relationship("FrequenciaProfessorTurmaMateria")