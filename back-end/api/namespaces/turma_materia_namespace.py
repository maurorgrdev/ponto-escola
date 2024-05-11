from flask_restx import Namespace, fields
from api.schemas import TurmaMateriaSchema, TurmaMateriasSchema, MateriaTurmasSchema 
from flask import Blueprint
from flask_restx import Api

turma_materia_ns = Namespace('turmas-materias', description='Operações relacionadas a alguma entidade')

turma_materia_schema = TurmaMateriaSchema()

turma_materias_schema = TurmaMateriasSchema()

materia_turmas_schema = MateriaTurmasSchema()