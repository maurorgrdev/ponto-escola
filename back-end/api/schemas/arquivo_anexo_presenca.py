from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.arquivo_anexo_frequencia import ArquivoAnexoFrequencia

class ArquivoSchema(SQLAlchemyAutoSchema):
        model = ArquivoAnexoFrequencia
        load_instance = True
