import socket

#define o endereço Ip do servidor
server_host = "localhost"
#define a porta do servidor
server_port = 5555

#cria um objeto socket para o cliente usando TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    #incia uma conexão com o servidor, especificando a endereço IP e a porta do servidor
    client_socket.connect((server_host, server_port))
    
    #loop infinito que irá permitir enviar sucessivas mensagens para o servidor
    while True:

        #mensagem a ser enviada para o servidor
        message = input("Digite uma mensagem (ou 'sair' para sair): ")

        #condição de parada do loop: 'sair'
        if message == "sair":
            break
        
        #transforma a mensagem em bytes e envia para o servidor
        client_socket.sendall(message.encode())

        #recebe a resposta do servidor, o 'recv' bloqueia a thread até que a mensagem seja recibida ou conexão seja fechada
        response = client_socket.recv(1024)

        #decodifica transformando para string e mostra a mensagem recebida do servidor em reverso
        print(f"Resposta recebida: {response.decode()}")
