import grpc
from concurrent import futures
from common.proto import post_service_pb2_grpc
import post_service
import asyncio
from config import settings


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    post_service_pb2_grpc.add_PostServiceServicer_to_server(
        post_service.PostService(), server)
    server.add_insecure_port(settings.insecure_port)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
