from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from dbendpoint.services import PostService

def grpc_handlers(server):
    app_registry = AppHandlerRegistry("dbendpoint", server)
    app_registry.register(PostService)