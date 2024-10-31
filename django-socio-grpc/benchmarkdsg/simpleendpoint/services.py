from django_socio_grpc import services
from django_socio_grpc.decorators import grpc_action
from simpleendpoint.grpc.simpleendpoint_pb2 import SimpleServiceGetCharResponse
from asgiref.sync import sync_to_async

class SimpleService(services.Service):
    @grpc_action(
        request=None,
        response=[{"name":"char", "type": "string"}]
    )
    @sync_to_async
    def GetChar(self, request, context):
        return SimpleServiceGetCharResponse(char="a")
