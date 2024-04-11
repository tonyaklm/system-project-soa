import grpc
from concurrent import futures
import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'proto'))
from proto import post_service_pb2_grpc

import logging
import PostService
import asyncio


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    post_service_pb2_grpc.add_PostServiceServicer_to_server(
        PostService.PostService(), server)
    server.add_insecure_port("0.0.0.0:8001")
    await server.start()
    logging.info("Server is listening at port :%d", 8001)
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
