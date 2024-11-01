from django_socio_grpc import services
from django_socio_grpc.decorators import grpc_action
from simpleendpoint.grpc.simpleendpoint_pb2 import (
  SimpleServiceGetCharResponse, 
  SimpleServiceGetBiggerFileAsBytesResponse, 
  SimpleServiceGetBiggerFileAsStringResponse, 
  SimpleServiceGetBiggerFileAsStructResponse, 
  SimpleServiceGetSmallerFileAsBytesResponse, 
  SimpleServiceGetSmallerFileAsStringResponse, 
  SimpleServiceGetSmallerFileAsStructResponse
)
from google.protobuf.struct_pb2 import Struct
from asgiref.sync import sync_to_async
from pathlib import Path
from django.conf import settings
import json

class SimpleService(services.Service):
    @grpc_action(
        request=None,
        response=[{"name":"char", "type": "string"}]
    )
    @sync_to_async
    def GetChar(self, request, context):
        return SimpleServiceGetCharResponse(char="a")    

    ##############################################################

    def _read_file_and_return_as_json(self, file_name):
        
        with open(Path(f"{settings.BASE_DIR}/simpleendpoint/assets/{file_name}")) as file:
            file_data = json.load(file)
        return file_data  
    
    @grpc_action(
        request=None,
        response=[{"name":"file_struct", "type": "google.protobuf.Struct"}]
    )
    @sync_to_async
    def GetSmallerFileAsStruct(self, request, context):
        file_data = self._read_file_and_return_as_json("generated_file_2MB.json")
        file_struct = Struct()
        file_struct.update(file_data)
        return SimpleServiceGetSmallerFileAsStructResponse(file_struct=file_struct)
    

    @grpc_action(
        request=None,
        response=[{"name":"file_struct", "type": "google.protobuf.Struct"}]
    )
    @sync_to_async
    def GetBiggerFileAsStruct(self, request, context):
        file_data = self._read_file_and_return_as_json("generated_file_10MB.json")
        file_struct = Struct()
        file_struct.update(file_data)
        return SimpleServiceGetBiggerFileAsStructResponse(file_struct=file_struct)
    

    ##############################################################

    def _read_file_and_return_as_binary(self, file_name):
        
        with open(Path(f"{settings.BASE_DIR}/simpleendpoint/assets/{file_name}"), "rb") as file:
            file_data = file.read()
        return file_data  
    
    @grpc_action(
        request=None,
        response=[{"name":"file_bytes", "type": "bytes"}]
    )
    @sync_to_async
    def GetSmallerFileAsBytes(self, request, context):
        file_data = self._read_file_and_return_as_binary("generated_file_2MB.json")
        return SimpleServiceGetSmallerFileAsBytesResponse(file_bytes=file_data)
    

    @grpc_action(
        request=None,
        response=[{"name":"file_bytes", "type": "bytes"}]
    )
    @sync_to_async
    def GetBiggerFileAsBytes(self, request, context):
        file_data = self._read_file_and_return_as_binary("generated_file_10MB.json")
        return SimpleServiceGetBiggerFileAsBytesResponse(file_bytes=file_data)
    

    ##############################################################

    def _read_file_and_return_as_string(self, file_name):
        
        with open(Path(f"{settings.BASE_DIR}/simpleendpoint/assets/{file_name}"), "r") as file:
            file_data = file.read()
        return file_data  
    
    @grpc_action(
        request=None,
        response=[{"name":"file_string", "type": "string"}]
    )
    @sync_to_async
    def GetSmallerFileAsString(self, request, context):
        file_data = self._read_file_and_return_as_string("generated_file_2MB.json")
        return SimpleServiceGetSmallerFileAsStringResponse(file_string=file_data)
    

    @grpc_action(
        request=None,
        response=[{"name":"file_string", "type": "string"}]
    )
    @sync_to_async
    def GetBiggerFileAsString(self, request, context):
        file_data = self._read_file_and_return_as_string("generated_file_10MB.json")
        return SimpleServiceGetBiggerFileAsStringResponse(file_string=file_data)
