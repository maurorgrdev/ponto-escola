from flask import Flask
from flask import Blueprint

from api.controllers.turma_materia_controller import turma_materia_ns
from api.controllers.turma_controller import turma_ns
from api.controllers.professor_controller import professor_ns
from api.controllers.materia_controller import materia_ns
from api.controllers.turma_professor_controller import turma_professor_ns
from api.controllers.professor_materia_controller import professor_materia_ns

def register_routes(api):
    
    api.add_namespace(turma_materia_ns)
    api.add_namespace(turma_ns)
    api.add_namespace(professor_ns)
    api.add_namespace(materia_ns)
    api.add_namespace(turma_professor_ns)
    api.add_namespace(professor_materia_ns)