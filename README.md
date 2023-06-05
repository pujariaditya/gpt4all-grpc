# GPT4All with gRPC

Welcome to the GPT4All with gRPC project! This project showcases the usage of gRPC (Google Remote Procedure Call) to create a procedure call mechanism for executing the GPT4All model on a server and retrieving the response through remote procedure calls.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The GPT4All with gRPC project demonstrates how to integrate gRPC into a GPT4All model setup. It allows clients to communicate with a gRPC server and execute the GPT4All model remotely. The server receives requests from clients, performs the necessary computations using the GPT4All model, and sends the response back to the client.

## Features

- gRPC-based procedure call: The project leverages gRPC to create a remote procedure call mechanism for executing the GPT4All model on the server and obtaining responses from the client.
- GPT4All model integration: The project demonstrates the integration of the GPT4All model within the server, enabling clients to access the power of the model remotely.
- Scalability and performance: Using gRPC allows for efficient communication between the server and client, enabling high performance and scalability for executing GPT4All-based procedures.

## Installation

To install and set up the project, follow these steps:

1. Clone the project repository:

   ```shell
   git clone https://github.com/adityapujari98/gpt4all-grpc.git
   cd gpt4all-grpc

2. Set up the virtual environment (recommended):

   ```shell
    python3 -m venv venv
    source venv/bin/activate

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt

4. Install gRPC tools:

   Run the following command to install gRPC tools, including the gRPC protocol buffer compiler (protoc):
    
   ```shell
    python -m pip install grpcio-tools

5. Generate gRPC code:

   In the project directory, run the following command to generate the gRPC code from the protocol buffer definition file (.proto):

   ```shell
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protos/model.proto

6. Download the GPT4All model:

   Obtain the GPT4All model by visiting the official GPT4All website at https://gpt4all.io/index.html. Once downloaded, place the model files in the pretrained_model/ directory of the project. 

7. Set up the server:

   Run the following command to start the gRPC server:

   ```shell
   python app.py

8. Set up the client:
 
   Open a separate terminal window.
   Run the following command to execute the client and communicate with the gRPC server:

   ```shell
   python client.py

You're all set! Now you can start using the project.

## Usage
To utilize the GPT4All with gRPC project, follow these steps:

Ensure that the gRPC server is running by executing python **app.py** in a terminal window.

Open a separate terminal window and run python **client.py** to start the gRPC client.

Use the client to make remote procedure calls to the GPT4All model on the server. You can specify the desired input for the GPT4All model and receive the response through the gRPC communication channel.

Customize the project as needed by modifying the server implementation, client code, or GPT4All integration to suit your requirements.

## Contributing
Contributions to this project are welcome! If you have any ideas, suggestions, or bug reports, please submit them as issues or create a pull request with your proposed changes.

When contributing, please ensure that your code follows the existing coding style and conventions. Additionally, provide appropriate documentation and tests for the added features or bug fixes.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code for both personal and commercial purposes.