import socket
import threading


#
# PROGRAMA CONEXAO 1-1
#

#determinar porta de conexão(disponiveis: 49152 a 65535): PENDENTE
def find_Open_Ports():
    for port in range(49152, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            sock.close()
            return port
        sock.close()

# socket udp
# thread rodando socket pra recebimento de arquivo-->função
recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_Port = find_Open_Ports()
connection_Addr = ('LOCALHOST', my_Port)
recv.bind = connection_Addr

def  recv_msg():
    while True:
        msgr, cliente = recv.recvfrom(1024)
        if msgr is not None:
            print("Mensagem recebida:", msgr)
            msgr = None

t = threading.Thread(target=recv_msg)
t.start()

while True:
    msg = input('Mensagem que voce deseja enviar:')
    recv.sendto(msg.encode(), '0.0.0.0')