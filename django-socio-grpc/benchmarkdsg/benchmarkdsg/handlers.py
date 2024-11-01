from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from simpleendpoint.handlers import grpc_handlers as simpleendpoint_handlers
from dbendpoint.handlers import grpc_handlers as dbenpoint_handlers

def grpc_handlers(server):
    simpleendpoint_handlers(server=server)
    dbenpoint_handlers(server=server)