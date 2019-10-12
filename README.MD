# Trabalho de Prática com Sockets

1. Introdução
2. UDP "Pinger"
3. Web Server

## 1. Introdução

O objetivo do trabalho é praticar a implementação de Sockets TCP e UDP. O
trabalho foi desenvolvido em Python.

![Alt Text](https://media.giphy.com/media/3oriNLx3dUqFgVi86I/giphy.gif)

## 2. UDP “Pinger”

Nesta questão, você aprenderá as noções básicas de programação de soquete para UDP em Python. Você aprenderá como enviar e receber pacotes datagramas usando soquetes UDP e também como definir um
tempo limite (“timeout”) de soquete apropriado.

Primeiro você estudará um servidor de Ping simples escrito em Python e implementará um cliente correspondente. A funcionalidade fornecida pelo cliente e servidor em Python é semelhante à fornecida pelos programas de Ping disponíveis nos sistemas operacionais modernos. No entanto, eles(cliente e servidor) usam um protocolo mais simples, o UDP, em vez do protocolo ICMP (Internet Control Message Protocol) para se comunicar entre si. O protocolo ping permite que uma máquina cliente envie um pacote de
dados para uma máquina remota e faça com que a máquina remota retorne os dados inalterados de volta ao cliente (uma ação chamada de “eco”). Entre outros usos, o protocolo ping permite que os hosts determinem
tempos de ida e volta (Round-Trip Time ou RTT) para outras máquinas.

### Código do Servidor

O código a seguir implementa um servidor de ping. O servidor simula 30% de perda dos pacotes que chegam.

```
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

```
### Perda de Pacotes

O UDP fornece às aplicações um serviço de transporte não confiável. As mensagens podem se perder na rede devido a sobrecargas na fila do roteador, a algum hardware defeituoso ou outros motivos. Já que a perda de pacotes pode ser rara ou até mesmo inexistente em redes LANs, o servidor em questão injeta perda artificial para simular seus efeitos. 

### Código do Cliente

 O cliente deve enviar 10 pings para o servidor. Como o UDP é um protocolo não confiável, um pacote enviado do cliente para o servidor pode ser perdido na rede ou vice-versa. Por esse motivo, o cliente não pode aguardar indefinidamente uma resposta a uma mensagem de ping. Então, fazemos com que o cliente espere até um segundo por uma resposta; Se nenhuma resposta for recebida dentro de um segundo, o programa cliente deve assumir que o pacote foi perdido durante a transmissão pela rede. Eu procurei a documentação do Python para descobrir como definir o valor de tempo limite (timeout) em um soquete de datagrama.

```
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

```

### Saídas

![](https://pbs.twimg.com/media/EGEutYTX0AEBiwU?format=jpg&name=large)

![](https://pbs.twimg.com/media/EGEutYUXUAAvjtI?format=jpg&name=large)


## 3. Web Server

![](http://appsbuilders.org/wp-content/uploads/2019/07/1562589463_maxresdefault-1140x641.jpg)

Nesta questão, você aprenderá os fundamentos da programação de soquetes para conexões TCP em Python: como criar um soquete, vinculá-lo a um endereço e porta específicos, bem como enviar e receber um pacote HTTP. Você também aprenderá algumas noções básicas de formato do cabeçalho HTTP.

a) Você desenvolverá um servidor Web que manipula apenas uma solicitação HTTP por vez. Seu servidor Web deve aceitar solicitações HTTP, obter páginas solicitadas pelo cliente, e também deve criar mensagens de resposta HTTP, constituída do arquivo solicitado precedido pelas linhas de cabeçalho e, então, enviar a resposta ao cliente. Se o arquivo solicitado não estiver presente no servidor, o servidor deverá enviar uma mensagem HTTP “404 Not Found” de volta ao cliente.

b) Implemente um servidor multithread capaz de atender a várias solicitações simultaneamente. Usando threading, primeiro crie um thread principal no qual o servidor atende clientes em uma porta fixa. Quando ele recebe uma solicitação de conexão TCP de um cliente, ele configura a conexão TCP através de outra porta e atender à solicitação do cliente em um thread separado. Haverá uma conexão TCP separada em um thread separado para cada par de solicitação/resposta.

c) Em vez de usar um navegador, escreva seu próprio cliente HTTP para testar seu servidor. Seu cliente se conectará ao servidor usando uma conexão TCP, enviará uma solicitação HTTP ao servidor e exibirá a resposta do servidor como uma saída. Você pode assumir que a solicitação HTTP enviada é um método GET. O cliente deve usar argumentos de linha de comando, especificando o endereço IP ou o nome do host do servidor, a porta na qual o servidor está atendendo e o caminho no qual o objeto solicitado é armazenado no servidor. A seguir está um formato de comando de entrada para executar o cliente.

**client.py server_host server_port nome_arquivo**

![](https://pbs.twimg.com/media/EGpmNYSXUAAIvQA?format=jpg&name=large)