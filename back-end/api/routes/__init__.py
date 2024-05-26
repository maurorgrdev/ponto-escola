from flask import Flask
from flask import Blueprint

from api.controllers.turma_materia_controller import turma_materia_ns
from api.controllers.turma_controller import turma_ns
from api.controllers.professor_controller import professor_ns
from api.controllers.materia_controller import materia_ns
from api.controllers.turma_professor_controller import turma_professor_ns
from api.controllers.professor_materia_controller import professor_materia_ns
from api.controllers.bimestre_controller import bimestre_ns
from api.controllers.tempo_controller import tempo_ns
from api.controllers.frequencia_professor_turma_materia_controller import frequencia_ns
from api.controllers.turma_plano_semanal_bimestre_controller import turma_plano_ns

def register_routes(api):
    
    api.add_namespace(turma_materia_ns)
    api.add_namespace(turma_ns)
    api.add_namespace(professor_ns)
    api.add_namespace(materia_ns)
    api.add_namespace(turma_professor_ns)
    api.add_namespace(professor_materia_ns)
    api.add_namespace(bimestre_ns)
    api.add_namespace(tempo_ns)
    api.add_namespace(frequencia_ns)
    api.add_namespace(turma_plano_ns)