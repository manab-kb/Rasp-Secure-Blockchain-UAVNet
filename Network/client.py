from socket import *
import pickle

# Class containing member functions and variables for implementation of a client
class client:
    # Constructor function to create a socket with the hostname and port number provided by the UAV
    def __init__(self, hostname, portnum):
        # Specifying loopback address as hostname alongsides accepting port number
        self.host = hostname
        self.port = portnum
        # Specifying hostname and portnumber for client socket to be binded to the ports within range
        self.chost = '0.0.0.0'
        self.cport = 33400
    
    # Function to connect to the GCS (server) and pass on data / blocks from the blockchain
    def serverConn(self, bdata):
        # Creating a TCP socket and using it to connect to the server socket
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.chost, self.cport))
        sock.connect((self.host, self.port))
        print("\n@log: Connected to GCS\n")
        # print(bdata)
        # Add code for sending blockchain data to the server
        bstream = pickle.dumps(bdata)
        sock.sendall(bstream)
        data = sock.recv(4096)
