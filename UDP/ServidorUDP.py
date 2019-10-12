import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12000))

while True:
    # Gera um número aleatório de 0 a 10
    rand = random.randint(0, 10)
    # Recebe do cliente o pacote junto com seu endereço de destino
    message, address = server_socket.recvfrom(1024)
    # Escreve a mensagem em letras maiúsculas
    message = message.upper()
    # Se rand < 4, consideramos que o pacote foi perdido
    if rand < 4:
        continue
    # Caso contrário, o servidor responde
    server_socket.sendto(message, address)