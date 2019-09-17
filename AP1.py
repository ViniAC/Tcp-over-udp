import socket
import threading

#

#determinar porta de conexão(disponiveis: 49152 a 65535): PENDENTE
def find_Open_Ports():
    for port in range(49152, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = sock.connect_ex((my_Ip, port))
        if result == 0:
            sock.close()
            return port
        sock.close()
#
#   PROGRAMA CONEXAO 1-1
#
# socket udp
# thread rodando socket pra recebimento de arquivo-->função
#

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_Host, my_Ip = get_Host_Name_Ip()
my_Port = find_Open_Ports()
print(my_Ip)
connection_Addr = (my_Host, my_Port)
udp.bind = connection_Addr

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