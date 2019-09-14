import socket

#INICIALIZAÇÃO:
#detectar hostname/ip
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        

#FUNCIONALIDADES:
#função aceitar novas conexões
#função 