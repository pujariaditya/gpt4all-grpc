import protos.model_pb2 as model_pb2
import protos.model_pb2_grpc as model_pb2_grpc


class ModelServicer(model_pb2_grpc.ModelServiceServicer):
    def __init__(self, model):
        self.llm = model

    def TextGenerate(self, request, context):
        message = request.message
        reply = self.llm(message)
        response = model_pb2.TextGenerateResponse(reply=reply)
        return response
