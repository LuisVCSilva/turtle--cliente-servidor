import StringIO
import socket
import turtle
import os
import json

pen = turtle.Pen();

def exemploDemo():
    pen.color("red","yellow")
    pen.begin_fill()
    for i in range(0,200):
        pen.forward(200)
        pen.left(170)
        if abs(pen.pos()) < 1:
            break
    pen.end_fill()

def case_1():
    exemploDemo()
def case_2():
    pen.forward(params[0])
def case_3():
    pen.back(params[0])
def case_4():
    pen.right(params[0])
def case_5():
    pen.left(params[0])
def case_6():
    pen.goto(params[0],params[1])
def case_7():
    pen.home()
def case_8():
    pen.circle(params[0],params[1])
def case_9():
    pen.dot(params[0])
def case_10():
    pen.color('#'+''.join(map(chr, (params[0],params[1],params[2]) )).encode('hex'),'#'+''.join(map(chr, (params[3],params[4],params[5]))).encode('hex'))
def case_default():
    print ''

dict = {"DEMO" : case_1,
	"FWD" : case_2,
	"BCK" : case_3,
	"RGT" : case_4,
	"LFT" : case_5,
	"GOTO" : case_6,
	"HOME" : case_7,
	"CIRC" : case_8,
	"DOT" : case_9,
	"COLOR" : case_10
}

def switch(x):

    try:
        dict[x]()
    except:
        case_default()


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
os.system("clear");
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    deMarsh, addr = sock.recvfrom(1024)

    data = str(json.loads(deMarsh))

    argumentos = data[data.index(",")+3:-2]
    comando = data.replace(argumentos,'')[2:].replace("', '')",'')

    comando.strip() 
    argumentos.strip()
    print "Executando comando:",comando," com args =",argumentos," enviado por [", addr, "]"
    
    msg = comando
    argumentos = argumentos.replace("(",'').replace(")",'')
    print(argumentos.split(","))
    params = list(map(int, argumentos.split(","))) 


    try:
        switch(msg)
    except:
        print 'Mensagem nao reconhecida'

    sock.sendto((str("TRUE")),addr)
    data = ""
