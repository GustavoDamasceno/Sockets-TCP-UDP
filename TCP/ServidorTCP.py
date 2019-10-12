import socket
import sys# para terminar o programa
 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Prepara o socket servidor
serverSocket.bind(('localhost', 12000))
serverSocket.listen(1)

while True: 
    print("Pronto para servir...")
    #Configurar uma nova conexão do cliente
    conexao, endereco = serverSocket.accept()

    try:
        #Recebe a mensagem de solicitação do cliente
        mensagem = conexao.recv(1024)
        print("Message is:", mensagem)
        #Extraia o caminho do objeto solicitado da mensagem
        #O caminho é a segunda parte do cabeçalho HTTP, identificado por [1]
        filename = mensagem.split()[1]
        print("nome do arquivo", filename)
        #Porque o caminho extraído da solicitação HTTP inclui
        #um caractere '/', lemos o caminho do segundo caractere
        f = open(filename[1:])
        # Armazena o contenet inteiro do arquivo solicitado em um buffer temporário
        outputdata = f.read()
        # Envie a linha do cabeçalho de resposta HTTP para o soquete de conexão
        conexao.send(bytes("HTTP / 1.1 200 OK\nContent-Type: index.html; charset=UTF-8\r\n\r\n".encode()))
        #Envia o conteúdo do arquivo solicitado ao cliente
        for i in range(0, len(outputdata)):
            conexao.send(outputdata[i].encode())
        conexao.send("\r\n".encode())
        conexao.close()
   
    except IOError:
        conexao.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        conexao.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        conexao.close

serverSocket.close()
sys.exit()#Termina o programa depois de enviar os dados

