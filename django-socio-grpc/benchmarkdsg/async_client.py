import asyncio
import grpc
from datetime import datetime
from simpleendpoint.grpc.simpleendpoint_pb2_grpc import SimpleServiceControllerStub 
from google.protobuf.empty_pb2 import Empty


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        # create Author gRPC client
        simple_service_client = SimpleServiceControllerStub(channel)

        # Create
        for i in range(10):
            simple_service_response = await simple_service_client.GetChar(Empty())
            print("author create response:", simple_service_response)  # flush=True


if __name__ == "__main__":
    asyncio.run(main())