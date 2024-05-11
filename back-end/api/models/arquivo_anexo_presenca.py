from api.config import db
from sqlalchemy import Column, Integer, ForeignKey, String, Date, Boolean
from sqlalchemy.orm import relationship

class ArquivoAnexoPresenca(db.Model):
    __tablename__ = 'arquivo'

    id = Column(Integer, primary_key=True)
    professor_presenca_id = Column(Integer, ForeignKey('presenca_professor_turma_materia.id'))
    caminho = Column(String) 
    tipo_arquivo = Column(String)
    nome_arquivo = Column(String)
    apelido = Column(String)
    tamanho = Column(Integer)
    
    presenca = relationship("PresencaProfessorTurmaMateria")