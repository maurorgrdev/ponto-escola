from marshmallow import Schema, fields, validate, validates, ValidationError

class TempoSchema(Schema):
    id = fields.Integer(dump_only=True)
    descricao = fields.String(required=True, validate=validate.Length(max=50))
    horario_inicio = fields.Time(required=True)
    horario_fim = fields.Time(required=True)

    # @validates('descricao')
    # def validate_descricao(self, value):
    #     if not value.startswith('A'):
    #         raise ValidationError('A descrição da tempo deve começar com a letra "A".')
