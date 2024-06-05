# app/service/resource_service.py

from app.repository.resource.resource_repository_interface import ResourceRepositoryInterface
from injector import inject

class MyResourceService:
    
    @inject
    def __init__(self, repository: ResourceRepositoryInterface):
        self.repository = repository

    def get_all_resources(self):
        return self.repository.get_all()

    def create_resource(self, data):
        return self.repository.create(data)

    def get_resource(self, resource_id):
        return self.repository.get_by_id(resource_id)

    def update_resource(self, resource_id, data):
        return self.repository.update(resource_id, data)

    def delete_resource(self, resource_id):
        return self.repository.delete(resource_id)
