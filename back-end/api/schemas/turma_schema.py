from marshmallow import Schema, fields, validate, validates, ValidationError

class TurmaSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True, validate=validate.Length(max=100))

    # @validates('descricao')
    # def validate_descricao(self, value):
    #     if not value.startswith('A'):
    #         raise ValidationError('A descrição da turma deve começar com a letra "A".')
