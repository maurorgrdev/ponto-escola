from flask import Blueprint
from .materia_routes import create_materia_blueprint
from .turma_routes import create_turma_blueprint
from .professor_routes import create_professor_blueprint
from .turma_materia_routes import create_turma_materia_blueprint
from .turma_professor_routes import create_turma_professor_blueprint
from .professor_materia_routes import create_professor_materia_blueprint

def register_routes(app):
    materia_bp = create_materia_blueprint()
    turma_bp = create_turma_blueprint()
    professor_bp = create_professor_blueprint()
    turma_materia_bp = create_turma_materia_blueprint()
    turma_professor_bp = create_turma_professor_blueprint()
    professor_materia_bp = create_professor_materia_blueprint()


    app.register_blueprint(materia_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_materia_bp)
    app.register_blueprint(turma_professor_bp)
    app.register_blueprint(professor_materia_bp)