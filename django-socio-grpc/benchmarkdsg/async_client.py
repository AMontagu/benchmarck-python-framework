import asyncio
import grpc
from datetime import datetime
from simpleendpoint.grpc.simpleendpoint_pb2_grpc import SimpleServiceControllerStub
from dbendpoint.grpc.dbendpoint_pb2_grpc import PostControllerStub
from dbendpoint.grpc.dbendpoint_pb2 import PostRequest, PostDestroyRequest
from google.protobuf.empty_pb2 import Empty


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        # create simple service gRPC client
        simple_service_client = SimpleServiceControllerStub(channel)

        ####################### SIMPLE TEST
        for i in range(10):
            simple_service_response = await simple_service_client.GetChar(Empty())
            print("author create response:", simple_service_response)  # flush=True

        
        ##################### DB CREATION TEST
        db_endpoint_client = PostControllerStub(channel)

        element_pks = []
        for i in range(10):
            request = PostRequest(pub_date=datetime.now().strftime("%Y-%m-%d"), headline="Test Perf", content="This is the content of the publication")
            create_response = await db_endpoint_client.Create(request)
            element_pks.append(create_response.id)

        ##################### DB Retrieve TEST


        
        # Clean up. No need to mesure
        for element_pk in element_pks:
            request = PostDestroyRequest(id=element_pk)
            await db_endpoint_client.Destroy(request)
        


        


if __name__ == "__main__":
    asyncio.run(main())