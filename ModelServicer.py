import protos.model_pb2 as model_pb2
import protos.model_pb2_grpc as model_pb2_grpc


class ModelServicer(model_pb2_grpc.ModelServiceServicer):
    def __init__(self, model):
        self.llm = model

    def process_string(self,message, reply):
        while True:
            if reply == "":
                reply = self.llm(message)
            else:
                return reply

    def TextGenerate(self, request, context):
        message = request.message
        initial_reply = ""
        final_reply = self.process_string(message, initial_reply)
        response = model_pb2.TextGenerateResponse(reply=final_reply)
        return response
