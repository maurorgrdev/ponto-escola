from app.model import Resource  
from .resource_repository_interface import ResourceRepositoryInterface
from app.configuration import db

class ResourceRepository(ResourceRepositoryInterface):

    def get_all(self):
        return Resource.query.all()

    def get_by_id(self, resource_id):
        return Resource.query.get(resource_id)

    def create(self, data):
        resource = Resource(**data)
        db.session.add(resource)
        db.session.commit()
        return resource

    def update(self, resource_id, data):
        resource = Resource.query.get(resource_id)
        if resource:
            for key, value in data.items():
                setattr(resource, key, value)
            db.session.commit()
            return resource
        return None

    def delete(self, resource_id):
        resource = Resource.query.get(resource_id)
        if resource:
            db.session.delete(resource)
            db.session.commit()
            return True
        return False
