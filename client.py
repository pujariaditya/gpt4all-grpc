import grpc

import protos.model_pb2 as model_pb2
import protos.model_pb2_grpc as model_pb2_grpc


class ModelClient:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = model_pb2_grpc.ModelServiceStub(self.channel)

    def generate_text(self, message):
        request = model_pb2.TextGenerateRequest(message=message)
        response = self.stub.TextGenerate(request)
        return response.reply


if __name__ == '__main__':
    server_address = 'localhost:5051'
    client = ModelClient(server_address)

    message = "what are the best places to visit in europe?"
    reply = client.generate_text(message)
    print(reply)
