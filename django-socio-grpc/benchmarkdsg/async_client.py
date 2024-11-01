import asyncio
import grpc
from datetime import datetime
from simpleendpoint.grpc.simpleendpoint_pb2_grpc import SimpleServiceControllerStub
from dbendpoint.grpc.dbendpoint_pb2_grpc import PostControllerStub
from dbendpoint.grpc.dbendpoint_pb2 import PostRequest, PostDestroyRequest, PostRetrieveRequest
from google.protobuf.empty_pb2 import Empty
from time import perf_counter


async def main():
    channel_options = [
        ("grpc.max_send_message_length", 1800 * 1024 * 1024),
        ("grpc.max_receive_message_length", 1800 * 1024 * 1024),
    ]
    async with grpc.aio.insecure_channel("localhost:50051", options=channel_options) as channel:
        # create simple service gRPC client
        simple_service_client = SimpleServiceControllerStub(channel)

        ####################### SIMPLE TEST
        # for i in range(10):
        #     simple_service_response = await simple_service_client.GetChar(Empty())
        #     print("author create response:", simple_service_response)  # flush=True

        
        # ##################### DB CREATION TEST
        db_endpoint_client = PostControllerStub(channel)

        element_pks = []
        for i in range(10):
            request = PostRequest(pub_date=datetime.now().strftime("%Y-%m-%d"), headline="Test Perf", content="This is the content of the publication")
            create_response = await db_endpoint_client.Create(request)
            element_pks.append(create_response.id)

        # ##################### DB Retrieve TEST
        for i in range(10):
            request = PostRetrieveRequest(id=element_pks[0])
            r = await db_endpoint_client.Retrieve(request)
            print(r)

        
        # # Clean up. No need to mesure
        # for element_pk in element_pks:
        #     request = PostDestroyRequest(id=element_pk)
        #     await db_endpoint_client.Destroy(request)
        

        # ##################### Retireve file json struct
        print("JSON Struct file")
        before_struct_small_response = perf_counter()
        struct_small_response = await simple_service_client.GetSmallerFileAsStruct(Empty())
        before_bigger_small_response = perf_counter()
        struct_bigger_response = await simple_service_client.GetBiggerFileAsStruct(Empty())

        # ##################### Retrieve file binary
        print("Binary file")
        before_binary_small_response = perf_counter()
        binary_small_response = await simple_service_client.GetSmallerFileAsBytes(Empty())
        before_binary_bigger_response = perf_counter()
        binary_bigger_response = await simple_service_client.GetBiggerFileAsBytes(Empty())

        # ##################### Retrieve file string
        print("String file")
        before_string_small_response = perf_counter()
        string_small_response = await simple_service_client.GetSmallerFileAsString(Empty())
        before_string_bigger_response = perf_counter()
        string_bigger_response = await simple_service_client.GetBiggerFileAsString(Empty())

        ############
        end_file_counter = perf_counter()

        print("Perf for file:")
        print(f"struct_small_response: {before_bigger_small_response - before_struct_small_response}")
        print(f"struct_bigger_response: {before_binary_small_response - before_bigger_small_response}")

        print(f"binary_small_response: {before_binary_bigger_response - before_binary_small_response}")
        print(f"binary_bigger_response: {before_string_small_response - before_binary_bigger_response}")

        print(f"string_small_response: {before_string_bigger_response - before_string_small_response}")
        print(f"string_bigger_response: {end_file_counter - before_string_bigger_response}")

        

        


if __name__ == "__main__":
    asyncio.run(main())