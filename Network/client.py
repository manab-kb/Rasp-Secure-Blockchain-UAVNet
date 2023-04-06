import sys
sys.dont_write_bytecode = True

from socket import *
import pickle
import random

# Class containing member functions and variables for implementation of a client
class client:
    # Constructor function to create a socket with the hostname and port number provided by the UAV
    def __init__(self, hostname, portnum):
        # Specifying loopback address as hostname alongsides accepting port number
        self.host = hostname
        self.port = portnum
        self.chost = '0.0.0.0'
        self.cport = random.randint(33334, 33999)

    # Function to connect to the GCS (server) and pass on data / blocks from the blockchain
    def serverConn(self, bdata, index, key):
        # Creating a TCP socket and using it to connect to the server socket
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((self.chost, self.cport))
        sock.connect((self.host, self.port))
        print("\n@log: Connected to GCS\n")

        enclist = []
        for i in bdata:
            for j in i:
                for k in j:
                    asci = int(ord(k))
                    enclist.append((asci + key) % 256)
        encryptblock = ''.join(chr(i) for i in enclist)
        encryptblock = bdata
        # print(bdata)
        # Add code for sending blockchain data to the server
        if index == '1':
            bstream = pickle.dumps(encryptblock)
            sock.sendall(bstream)
            data = sock.recv(4096)
