from abc import ABC, abstractmethod

class ResourceRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, resource_id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, resource_id, data):
        pass

    @abstractmethod
    def delete(self, resource_id):
        pass
