import socket
import threading
#INICIALIZAÇÃO:
#detectar hostname/ip
class Con_List:
    def __init__(self):
        self.list = []
    def append_list(ip):
        list.append(ip)
class Socket_List:
    def __init__(self):
        self.socketlist = []
    def append_list(socket):
        socketlist.append(socket)
class Socket:
    def __init__(self, ip):
        self.socketIp = ip
class ASocket:
    def __init__(self, ip):
        self.socketIp = ip
    #SEPARAR ASocket de MY_PC e gerar ela quando o programa startar
class My_Pc:
    def new_client_socket():
        return 0  
    def __init__(self, host_name, host_ip, asocket, con_list):
        self.host_name = host_name
        self.host_ip = host_ip
        self.asocket = asocket
        self.usersList = con_list
class Connected_PCs:
    def __init__(self, con_name, con_ip):
        self.con_name = con_name
        self.con_ip = con_ip
#Initializing:
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name,host_ip
    except:
        print("Unable to get Hostname and IP")

def create_accept_socket():
       if not'ACsocket' in globals():
            ACsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return ACsocket
def accept_connection():
    if not 'ACthread' in globals():
            ACthread = threading.Thread(target=accept_connection)
            ACthread.start()
    while True:
            conMsg, client = ACthread.recvfrom(1024)
            if conMsg[2:-1] == 'SYN' and client not in MyPc.usersList:
                new_client_socket(client)
ACsocket = create_accept_socket
accept_connection
Phostname, Phostip = get_Host_name_IP()
ConList = Con_List   
SocketList = Socket_List
MyPc = My_Pc(Phostname, Phostip, ConList, SocketList)
#FUNCIONALIDADES:
#Criar novas conexões
#função 