import time
import socket
from datetime import datetime


for pings in range(1, 11):
    #Cria o socket cliente IPV4  e socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Tempo limite de 1 segundo
    client_socket.settimeout(1)

    mensagem = 'Pacote enviado porraaaa'
    mensagem = mensagem.encode()

    address = ("localhost", 12000)

    start = time.time()

    #Cliente socket envia o que há na variável mensagem para o IP e porta;
    client_socket.sendto(mensagem, address)

    data_e_hora_atuais = datetime.now()
    #Transformando o datatime em string
    data_e_hora_string = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M') 

    try:
        mensagem, server = client_socket.recvfrom(1024)
        #tempo de ida
        ida = time.time()
        #Tempo de resposta em cada pacote em segundos
        RTT = ida - start
        print("Ping: " + str(pings) + " Data e Hora: " + data_e_hora_string + " Mensagem do servidor: " + str(mensagem) +  " RTT: " + str(RTT))
    except socket.timeout:
        print("Pacote foi perdido durante a transmissão")
