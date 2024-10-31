from simpleendpoint.handlers import grpc_handlers as simpleempoint_handlers
from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

def grpc_handlers(server):
    simpleempoint_handlers(server=server)