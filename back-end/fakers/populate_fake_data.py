import sys
import os

# Adicione o diretório do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from faker import Faker
from datetime import datetime, timedelta
from api.app import create_app  # Importando a função create_app do módulo app

# Importando os modelos do pacote api
from api.config import db
from api.models.professor import Professor
from api.models.materia import Materia
from api.models.turma import Turma
from api.models.turma_plano_semanal_bimestre import TurmaPlanoSemanalBimestre
from api.models.frequencia_professor_turma_materia import FrequenciaProfessorTurmaMateria
from api.models.bimestre import Bimestre
from api.models.tempo import Tempo

fake = Faker()

app = create_app()  # Criando a instância do aplicativo

def create_fake_professores(n):
    professores = []
    for _ in range(n):
        professor = Professor(
            nome=fake.name()
        )
        professores.append(professor)
        db.session.add(professor)
    db.session.commit()
    return professores

def create_fake_materias(n):
    materias = []
    for _ in range(n):
        materia = Materia(
            nome=fake.word()
        )
        materias.append(materia)
        db.session.add(materia)
    db.session.commit()
    return materias

def create_fake_bimestres(n):
    bimestres = []
    start_date = datetime.now()
    for i in range(n):
        end_date = start_date + timedelta(weeks=9)  # Supondo que cada bimestre tem 9 semanas
        bimestre = Bimestre(
            descricao=f"Bimestre {i+1}",
            data_inicio=start_date,
            data_fim=end_date
        )
        bimestres.append(bimestre)
        db.session.add(bimestre)
        start_date = end_date + timedelta(days=1)  # Próximo bimestre começa no dia seguinte ao término do anterior
    db.session.commit()
    return bimestres

def create_fake_tempos(n):
    tempos = []
    for _ in range(n):
        start_time = fake.time_object()
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(hours=1)).time()  # Supondo que cada período dura 1 hora
        tempo = Tempo(
            descricao=fake.word(),
            horario_inicio=start_time,
            horario_fim=end_time
        )
        tempos.append(tempo)
        db.session.add(tempo)
    db.session.commit()
    return tempos

def create_fake_turmas(n):
    turmas = []
    professores = Professor.query.all()
    materias = Materia.query.all()
    bimestres = Bimestre.query.all()
    tempos = Tempo.query.all()

    for _ in range(n):
        turma = Turma(
            nome=fake.word()
        )
        db.session.add(turma)
        db.session.flush()  # Garante que a turma tenha um ID

        # Adicionando relacionamentos com professores e matérias
        turma.professores = random.sample(professores, random.randint(1, 3))
        turma.materias = random.sample(materias, random.randint(1, 3))
        
        # Adicionando relacionamento com planos semanais bimestrais
        turma_planos = []
        for _ in range(random.randint(1, 5)):
            plano = TurmaPlanoSemanalBimestre(
                turma=turma,
                dia_semana=fake.day_of_week(),
                bimestre=random.choice(bimestres),
                tempo=random.choice(tempos),
                materia=random.choice(turma.materias),
                professor=random.choice(turma.professores)
            )
            turma_planos.append(plano)
            db.session.add(plano)
        turma.planos = turma_planos

        turmas.append(turma)
    db.session.commit()
    return turmas

def create_fake_frequencias(planos, n):
    frequencias = []
    for _ in range(n):
        plano = random.choice(planos)
        frequencia = FrequenciaProfessorTurmaMateria(
            plano=plano,
            data=fake.date_this_year(),
            presente=random.choice([True, False])
        )
        frequencias.append(frequencia)
        db.session.add(frequencia)
    db.session.commit()
    return frequencias

# Usando o contexto do aplicativo para acessar o banco de dados
with app.app_context():
    # Criar dados falsos
    professores = create_fake_professores(10)
    materias = create_fake_materias(5)
    bimestres = create_fake_bimestres(4)  # Supondo 4 bimestres
    tempos = create_fake_tempos(6)  # Supondo 6 períodos
    turmas = create_fake_turmas(5)
    create_fake_frequencias([plano for turma in turmas for plano in turma.planos], 50)

    print("Fake data inserted successfully!")
