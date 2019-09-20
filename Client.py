import socket
import threading
import sys
import time
import pickle

local = '127.0.0.1', 10001
con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
con.bind(local)
dest = '127.0.0.1', 10000
class tcp_header:
    source_port_number = None
    destination_port_number = None
    sequence_number = None
    acknowledgement_number = None
    window_size = None
    syn = False
    ack = False
    fin = False
    rst = False
    
    def __init__(self, syn):
        self.syn = syn


x = tcp_header(True)
data_string = pickle.dumps(x)
while True:
    con.sendto(data_string, dest)
    while True:
        data, client = con.recvfrom(2048)
        tcpHeader = pickle.loads(data)
        if tcpHeader.syn == True and tcpHeader.ack == True:
            print(tcpHeader.syn)
            print(tcpHeader.ack)
