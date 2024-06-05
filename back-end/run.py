from app import create_app
from flask_injector import FlaskInjector
from injector import Binder, singleton
from app.repository.resource.resource_repository import ResourceRepository
from app.repository.resource.resource_repository_interface import ResourceRepositoryInterface

app = create_app()

def configure(binder: Binder) -> Binder:
    binder.bind(ResourceRepositoryInterface, to=ResourceRepository, scope=singleton)

FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    app.run(debug=True)
