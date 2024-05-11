class Config:
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@escola_flask-db-1/escola'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/escola'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Outras configurações relevantes aqui

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # Outras configurações específicas de desenvolvimento aqui

class ProductionConfig(Config):
    # Configurações específicas de produção aqui
    pass

# Adicione outras classes de configuração conforme necessário, como para ambientes de teste, etc.
