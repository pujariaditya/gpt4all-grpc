from concurrent import futures

import grpc
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All

import protos.model_pb2_grpc as model_pb2_grpc
from ModelServicer import ModelServicer

class ModelServer:
    def __init__(self, server_address, model_path, max_workers=10):
        self.server_address = server_address
        self.model_path = model_path
        self.max_workers = max_workers

    def run(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.max_workers))
        model = GPT4All(model=self.model_path, callbacks=[StreamingStdOutCallbackHandler()], verbose=True)
        model_servicer = ModelServicer(model)
        model_pb2_grpc.add_ModelServiceServicer_to_server(model_servicer, server)
        server.add_insecure_port(self.server_address)
        server.start()
        print("Server started")
        server.wait_for_termination()
