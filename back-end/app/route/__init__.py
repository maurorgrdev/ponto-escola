from ..controller.resource_controller import api as my_resource_ns

def register_routes(api, app, root="api"):
    api.add_namespace(my_resource_ns, path=f"/{root}/my_resource")
