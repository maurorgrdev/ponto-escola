from marshmallow import Schema, fields, validate, validates, ValidationError

class BimestreSchema(Schema):
    id = fields.Integer(dump_only=True)
    descricao = fields.String(required=True, validate=validate.Length(max=50))
    data_inicio = fields.Date(required=True)
    data_fim = fields.Date(required=True)

    # @validates('descricao')
    # def validate_descricao(self, value):
    #     if not value.startswith('A'):
    #         raise ValidationError('A descrição da bimestre deve começar com a letra "A".')
