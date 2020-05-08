import socket 
import json
import sys
import os


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = ""


opcoesLista = [
("DEMO","Criar Desenho Exemplo"),
("FWD","Mover a tartaruga para frente"),
("BCK","Mover a tartaruga para tras"),
("RGT","Girar a tartaruga para a direita"),
("LFT","Girar a tartaruga para a esquerda"),
("GOTO","Mover a tartaruga a uma posicao especifica"),
("HOME","Mover a tartaruga a posicao inicial"),
("CIRC","Fazer um circulo",),
("DOT","Marcar um ponto"),
("COLOR","Alterar a cor")
]
opCode = -1;

while True:
    while(not(opCode>=1 and opCode<=len(opcoesLista))):        
	os.system("clear");
        print "\nEndereco da maquina das tartarugas (servidor):", UDP_IP
        print "Porta utilizada na comunicacao", UDP_PORT

        print "\nO que voce deseja fazer:\n\n"
	for i in range(0,len(opcoesLista)):
            print " ", i+1, " >> " , opcoesLista[i][1] 



        opCode = int(input("Escolha = "))
        print "Entre com os parametros: "
        params = str(input("Parametros = "))
        MESSAGE = json.dumps(str((opcoesLista[opCode-1][0],params)))

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    opCode = -1
