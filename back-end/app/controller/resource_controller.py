# app/controllers/my_resource_controller.py

from flask import jsonify
from flask_restx import Namespace, Resource, fields
from injector import inject
from ..service.resource_service import MyResourceService
from ..schema.resource_schema import ResourceSchema
from ..decorator.decorator_response import standard_response

api = Namespace('my_resource', description='My Resource operations')

example_model = api.model('ExampleModel', {
    'name': fields.String(required=True, description='The resource name')
})


@api.route('/')
class MyResourceList(Resource):
    @inject
    def __init__(self, my_resource_service: MyResourceService, resource_schema: ResourceSchema, *args, **kwargs):
        self.my_resource_service = my_resource_service
        self.resource_schema = resource_schema
        super().__init__(*args, **kwargs)

    @api.doc('list_resources')
    @standard_response
    def get(self):
        '''List all resources'''
        payload = self.my_resource_service.get_all_resources()

        return self.resource_schema.dump(payload, many=True)

    @api.doc('create_resource')
    @api.expect(example_model)
    @standard_response
    def post(self):
        '''Create a new resource'''
        payload = self.my_resource_service.create_resource(api.payload)

        return self.resource_schema.dump(payload), 201

@api.route('/<int:id>')
@api.response(404, 'Resource not found')
@api.param('id', 'The resource identifier')
class MyResource(Resource):
    @inject
    def __init__(self, my_resource_service: MyResourceService, resource_schema: ResourceSchema, *args, **kwargs):
        self.my_resource_service = my_resource_service
        self.resource_schema = resource_schema
        super().__init__(*args, **kwargs)

    @api.doc('get_resource')
    @api.marshal_with(example_model)
    @standard_response
    def get(self, id):
        '''Fetch a resource given its identifier'''
        payload = self.my_resource_service.get_resource(id)

        return self.resource_schema.dump(payload), 200

    @api.doc('update_resource')
    @api.expect(example_model)
    @api.marshal_with(example_model)
    def put(self, id):
        '''Update an existing resource'''
        payload = self.my_resource_service.update_resource(id, api.payload)
    
        return self.resource_schema.dump(payload), 200

    @api.doc('delete_resource')
    @api.response(204, 'Resource deleted')
    def delete(self, id):
        '''Delete a resource given its identifier'''
        payload = self.my_resource_service.delete_resource(id)

        return self.resource_schema.dump(payload), 204
