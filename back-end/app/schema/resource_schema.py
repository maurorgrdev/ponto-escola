from marshmallow import Schema, fields

class ResourceSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
