import socket
import threading

#
# # detectar ip proprio e determinar porta de conexão:PENDENTE
def get_Host_Name_Ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name,host_ip
    except:
        print("Unable to get Hostname and IP")
#   PROGRAMA CONEXAO 1-1
#
# socket udp
# thread rodando socket pra recebimento de arquivo-->função
#

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
myHost, myIP = get_Host_Name_Ip()
print(myHost ,myIP)
myAddr = (myHost, myIP)
udp.bind(myAddr)

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