from marshmallow import Schema, fields, validate, ValidationError

class MateriaSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True, validate=validate.Length(max=100))
