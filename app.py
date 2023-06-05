from ModelServer import ModelServer

if __name__ == '__main__':
    server_address = '[::]:5051'
    model_path = 'pretrained_model/ggml-gpt4all-j-v1.3-groovy.bin'
    server = ModelServer(server_address, model_path)
    server.run()