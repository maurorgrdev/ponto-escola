from .turma_namespace import turma_ns, turma_model, turma_schema
from .materia_namespace import materia_ns, materia_model, materia_schema
from .professor_namespace import professor_ns, professor_model, professor_schema
from .turma_materia_namespace import turma_materia_ns, \
    turma_materia_model, turma_materia_schema, turma_materias_schema, materia_turmas_schema
from .turma_professor_namespace import turma_professor_ns, \
    turma_professor_model, turma_professor_schema, turma_professores_schema, professor_turmas_schema
from .professor_materia_namespace import professor_materia_ns, \
    professor_materia_model, professor_materia_schema, professor_materias_schema, materia_professores_schema