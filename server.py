import socket
import threading
import sys
import time
import pickle

thread_list = []
socket_list = []
def get_Host_Name_Ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        print("Unable to get Hostname and IP")

Host = '127.0.0.1'
Port = 10000
code = 1

connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MyIp = (Host, Port)
connection_socket.bind(MyIp)
socket_list.append(connection_socket)

def recv_con():
    while True:
        data, client = connection_socket.recvfrom(2048)
        tcpHeader = pickle.loads(data)
        if tcpHeader.syn == True:
            check_recv_connection(tcpHeader, client)

def check_recv_connection(header, client):
    if header.syn == True:
        print('Conexão recebida, enviando confirmação...')
        time.sleep(1)
        global code   
        connection_object = tcp_header(True, True, code)
        code = code + 1
        data_byte = pickle.dumps(connection_object)
        connection_socket.sendto(data_byte, client)
        server_socket ,connection_object.source_port_number = socket_manager(connection_object)
        threading.current_thread().setName(name= code)
        recv_message(connection_object, server_socket)

#função que vai rodar na thread pra receber mensagem de uma conexão nova
def recv_message(connection_object, server_socket):
    while True:
        data, client = server_socket.recvfrom(3096)


def find_Open_Ports():
    for port in range(49152, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            sock.close()
            return port
        sock.close()

def socket_manager():
    global socket_list
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketIpPort = (Host, find_Open_Ports())
    connection_socket.bind('127.0.0.1',socketIpPort)
    socket_list.append(connection_socket)
    return connection_socket, socketIpPort

#Main Thread = gerenciador de threads, New Connection Thread = thread para receber novas conexoes
def manage_thread():
    global thread_list
    if thread_list[0].name != 'Thread Principal':
        thread = threading.Thread(target=recv_con, name='Thread Principal')
        thread_list.append(thread)
        for x in range(len(thread_list)):
            if thread_list[x].name == 'Thread Principal':
                thread_list[0], thread_list[x] = thread_list[x], thread_list[0]
        thread.start()
        time.sleep(2)

manage_thread()
#thread = threading.Thread(target=manage_thread, name='Main Thread')
#thread_list.append(thread)

def create_socket():
    return 0

class tcp_header:
    code = None
    source_port_number = None
    destination_port_number = None
    sequence_number = None
    acknowledgement_number = None
    window_size = None
    syn = False
    ack = False
    fin = False
    rst = False
    msg = None

    def __init__(self, syn, ack, code):
        self.syn = syn
        self.ack = ack
        self.code = code

    def read_msg():
        return msg
    def write_msg(msgr):
        self.msg = msgr

#x = cabecalho_tcp
#print(sys.getsizeof(x))
