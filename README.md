# Simple TCP Client-Server Application

## Description

This project consists of a simple client-server application using TCP/IP. The server waits for client connections, receives messages, reverses these messages, and sends them back to the client. The client connects to the server, sends messages, and displays the response, which is the original message reversed.

## Project Structure

- `server.py`: Implements the TCP server that accepts client connections, receives messages, and sends back the reversed message.
- `client.py`: Implements the TCP client that connects to the server, sends messages, and displays the reversed response received from the server.

## How It Works

### Server (`server.py`)

1. The server listens on a specified IP address and port (in this case, port `5555`).
2. When a client connects, the server starts a new thread to handle the client's connection.
3. The server receives messages from the client, reverses the message string, and sends the reversed string back to the client.
4. The server continues to run, waiting for new client connections, and handles each connection in a separate thread.

### Client (`client.py`)

1. The client connects to the server using the specified IP address and port (`localhost` and `5555`).
2. The client enters a loop where it can send messages to the server.
3. The client sends the input message to the server and waits for the server's response.
4. The client receives and prints the server's response (the reversed message).
5. The client can exit the loop and close the connection by typing "exit".

## Usage Instructions

### Running the Server

1. Open a terminal and navigate to the directory containing `server.py`.
2. Run the server script:

    ```bash
    python server.py
    ```

3. The server will start and listen for client connections on port `5555`.

### Running the Client

1. Open a new terminal window and navigate to the directory containing `client.py`.
2. Run the client script:

    ```bash
    python client.py
    ```

3. The client will connect to the server running on `localhost` and port `5555`.

4. Enter messages to send to the server. The server will return the reversed message, which will be displayed in the terminal.

5. To disconnect, type `exit` and the client will close the connection.

### Example Interaction

**Server Output:**

```plaintext
Server listening on port 5555...
New connection received from 127.0.0.1:12345
Connection with 127.0.0.1:12345 closed.

## Cliente Interaction:

```
Enter a message (or 'exit' to quit): hello
Response received: olleh
Enter a message (or 'exit' to quit): world
Response received: dlrow
Enter a message (or 'exit' to quit): exit
```

## Notes

- Make sure the server is running before starting the client.
- Both scripts are designed to run on the same machine (localhost). To run on different machines, update the server_host in client.py with the server's IP address.
