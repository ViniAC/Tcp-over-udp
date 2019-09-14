import socket
import threading

Host = '127.0.0.1'
Port = 10000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MyIp = (Host, Port)
udp.bind(MyIp)

def  recv_msg():
    while True:
        msgr, cliente = udp.recvfrom(1024)
        if msgr is not None:
            print("Mensagem recebida:", msgr)
            msgr = None

t = threading.Thread(target=recv_msg)
t.start()

while True:
    msg = input('Mensagem que voce deseja enviar:')
    udp.sendto(msg.encode(), MyIp)