import sys
sys.dont_write_bytecode = True

from socket import *
from threading import *
import os
import pickle

# Class containing member functions and variables for a multithreaded server implementation
class multithreadServer(object):
    # Constructor function to create a socket with the hostname and port number provided by the GCS
    def __init__(self, hostname, portnum, key):
        self.host = hostname
        self.port = portnum
        self.key = key

        # Creation and binding a TCP soclet with socket options set to resue addresses once clients are disconnected
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    # Function which actively listens for UAVs(clients) to connect to the itself and creates threads for each connection from an UAV
    def listen(self):
        self.sock.listen(10)
        while True:
            client, add = self.sock.accept()
            print("\n@log: UAV connected: " + str(add) + "\n")
            Thread(target = self.recvData, args = (client,)).start()

    # Function which helps in writing the contents of the blockchain to global central database
    def writetoDb(self, data):
        # Opening and writing to the created database for the blockchain
        dbname = "College Green.txt"
        tempdbname = "TempCollegeGreen.txt"
        os.chdir("/users/ugrad/biswasma/Desktop/CN-Data-Fabric-Provider/GCS")
        writefile = open(dbname, "w")
        writefile.write(data)
        writefile.close()

    def encrypt(self, message):
        declist = []
        for i in message:
            asci = int(ord(i))
            declist.append((asci - self.key) % 256)
        decryptblockData = ''.join(chr(i) for i in declist)
        return decryptblockData

    # Function which helps in receiving data from the UAV's (clients) - function to be executed by each running thread
    def recvData(self, client):
        blockData = ""
        size = 4096
        while True:
            try:
                data = client.recv(size)
                if data:
                    blockData = pickle.loads(data)
                    dmesg = self.encrypt(blockData)
                    self.writetoDb(str(blockData))
                    # print(blockData)
                client.close()
            except:
                # client.close()
                # return False
                # Possibility of UAV disconnection as data is not being received by the server
                # raise error("@log: possibility of UAV disconnection.")
                pass
