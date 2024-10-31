from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from simpleendpoint.services import SimpleService

def grpc_handlers(server):
    app_registry = AppHandlerRegistry("simpleendpoint", server)
    app_registry.register(SimpleService)