# services/turma_plano_semanal_bimestre_service.py

from api.config import db
from api.models.turma_plano_semanal_bimestre import TurmaPlanoSemanalBimestre

class TurmaPlanoSemanalBimestreService:

    @staticmethod
    def get_all():
        return TurmaPlanoSemanalBimestre.query.all()

    @staticmethod
    def get_by_id(id):
        return TurmaPlanoSemanalBimestre.query.get(id)

    @staticmethod
    def create(data):
        plano = TurmaPlanoSemanalBimestre(**data)
        db.session.add(plano)
        db.session.commit()
        return plano

    @staticmethod
    def update(id, data):
        plano = TurmaPlanoSemanalBimestre.query.get(id)
        if plano:
            for key, value in data.items():
                setattr(plano, key, value)
            db.session.commit()
        return plano

    @staticmethod
    def delete(id):
        plano = TurmaPlanoSemanalBimestre.query.get(id)
        if plano:
            db.session.delete(plano)
            db.session.commit()
        return plano
