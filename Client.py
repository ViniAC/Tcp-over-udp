import socket
import pickle
import hashlib
local = '127.0.0.1', 50001
con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
con.bind(local)
dest = '127.0.0.1', 50000


class tcp_header:
    sequence_number = None
    acknowledgement_number = None
    syn = False
    ack = False
    fin = False
    rst = False
    file = None
    hash = None

    def __init__(self, syn, sequence_number, file, fin, hash):
        self.syn = syn
        self.sequence_number = sequence_number
        self.file = file
        self.fin = fin
        self.hash = hash

class table():
    buffer_list = []
    tcpHeader = tcp_header
    rst = False


count = 100


def End_connection():
    print("enviando confirmção...")
    connection_object = tcp_header(False, None, None, True, None)
    data_byte = pickle.dumps(connection_object)
    con.sendto(data_byte, server)


def Wait_confirmation():
    global count
    aux = 1
    print("Esperando confirmação...")
    data, server = con.recvfrom(2048)
    table.tcpHeader = pickle.loads(data)
    if table.tcpHeader.rst:
        table.rst = True
    while table.tcpHeader.acknowledgement_number != count - 99 and not table.rst:
        try:
            con.settimeout(5)
            print("Retransmitindo dado...")
            connection_object = tcp_header(False, count - 100 * aux, table.buffer_list[-1 - (-1*aux)].file, False, table.buffer_list[-1 - (-1*aux)].hash)
            data_byte = pickle.dumps(connection_object)
            con.sendto(data_byte, server)
            print("Esperando confirmação...")
            data, server = con.recvfrom(2048)
            table.tcpHeader = tcpHeader
            table.tcpHeader = pickle.loads(data)
        except socket.timeout:
            print("Retransmitindo")
            con.settimeout(None)
            aux = aux + 1
        except IndexError:
            aux = 1


def Send_file(buffer, hash_buffer):
    global count
    connection_object = tcp_header(False, count, buffer, False, hash_buffer)
    table.buffer_list.append(connection_object)
    data_byte = pickle.dumps(connection_object)
    con.sendto(data_byte, server)
    count = count + 100
    print("Enviando arquivo...")
    buffer = None
    Wait_confirmation()
    return buffer


def Split_file():
    buffer_size = 64000
    f = open("teste.mp4", "rb")
    buffer = f.read(buffer_size)
    while buffer:
        new = buffer.strip()
        hash_buffer = hashlib.md5(new).hexdigest()
        Send_file(buffer, hash_buffer)
        buffer = f.read(buffer_size)
    End_connection()

confirmation = False
while confirmation is not True:
    try:
        con.settimeout(10)
        connection_object = tcp_header(True, None, None, False, None)
        data_string = pickle.dumps(connection_object)
        print("Iniciando conexão")
        con.sendto(data_string, dest)
        print("Esperando confirmação de conexão")
        data, server = con.recvfrom(2048)
        tcpHeader = pickle.loads(data)
        if tcpHeader.rst:
            table.rst = True
        if tcpHeader.syn and tcpHeader.ack and not table.rst:
            Split_file()
        confirmation = True
    except socket.timeout:
        print("TIMEOUT, encerrando conexão...")
