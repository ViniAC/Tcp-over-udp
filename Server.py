import socket
import time
import pickle
import hashlib

server_ip = '127.0.0.1'
server_port = 50000
client = None

connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_address = (server_ip, server_port)
connection_socket.bind(my_address)


def Recv_con():
    while True:
            connection_socket.settimeout(None)
            print("Aguardando conexão")
            data, client = connection_socket.recvfrom(1024)
            tcpHeader = pickle.loads(data)
            Make_con(tcpHeader, client)

def Make_con(header, client):
    print("Validando conexão...")
    if header.syn == True:
        print('Conexão recebida, enviando confirmação...')
        time.sleep(1)
        connection_object = tcp_header(True, True, False)
        data_byte = pickle.dumps(connection_object)
        connection_socket.sendto(data_byte, client)
        Recv_files()


def Send_conf(tcpheader, client):
    print("Enviando confirmação de recebimento...")
    confirmation_object = tcpheader
    confirmation_object.file = None
    confirmation_object.acknowledgement_number = confirmation_object.sequence_number + 1
    data_byte = pickle.dumps(confirmation_object)
    connection_socket.sendto(data_byte, client)
    return confirmation_object.acknowledgement_number

def Send_failure(tcpheader, client):
    print("Enviando confirmação de arquivo corrompido...")
    confirmation_object = tcpheader
    confirmation_object.file = None
    confirmation_object.acknowledgement_number = confirmation_object.sequence_number - 99
    data_byte = pickle.dumps(confirmation_object)
    connection_socket.sendto(data_byte, client)

def Recv_files():
    global client
    tcpheader = tcp_header(False, False, False)
    cur_ack = 0
    exec_numb = 0
    connection_socket.settimeout(10)
    try:
        while tcpheader.fin is False:
            print("Recebendo Arquivo...")
            data, client_ = connection_socket.recvfrom(664000)
            if client is None:
                client = client_
            tcpheader = pickle.loads(data)
            buffer = open("copia.mp4", "ab")
            if tcpheader.fin:
                break
            if client != client_:
                rst_object = tcp_header(False, False, True)
                data_byte = pickle.dumps(rst_object)
                connection_socket.sendto(data_byte, client_)
            if tcpheader.file is not None:
                new = tcpheader.file.strip()
                local_hash = hashlib.md5(new).hexdigest()
                if client == client_ and local_hash == tcpheader.hash and tcpheader.sequence_number - 99 == cur_ack or exec_numb == 0:
                    buffer.write(tcpheader.file)
                    cur_ack = Send_conf(tcpheader, client)
                    print(tcpheader.sequence_number)
                    print(cur_ack)
                    exec_numb = 1
            elif client == client_ or tcpheader.fin is False or local_hash != tcpheader.hash or tcpheader.sequence_number - 99 != cur_ack:
                print(cur_ack)
                Send_failure(tcpheader, client)

        buffer.close()
        client = None
        print("Arquivo recebido com sucesso!")
    except socket.timeout:
        print("TIMEOUT, encerrando conexão!")
        client = None


class tcp_header:
    sequence_number = None
    acknowledgement_number = None
    syn = False
    ack = False
    fin = False
    rst = False
    file = None
    hash = None

    def __init__(self, syn, ack, rst):
        self.syn = syn
        self.ack = ack
        self.rst = rst
Recv_con()