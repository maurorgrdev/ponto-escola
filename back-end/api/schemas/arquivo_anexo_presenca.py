from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.arquivo_anexo_presenca import ArquivoAnexoPresenca

class ArquivoSchema(SQLAlchemyAutoSchema):
        model = ArquivoAnexoPresenca
        load_instance = True
