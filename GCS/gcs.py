import sys
sys.dont_write_bytecode = True

from Blockchain.blockchain import *
from Network.server import *
import os

# Class containing member functions and variables for the Ground Control Station(GCS)
class GCS(Blockchain, multithreadServer):

    # Constructor function to declare and initialise all member variables being used alongside calling the superclass
    def __init__(self, clients):
        Blockchain.__init__(self, 0, 250)

        # Creating a database for the blockchain
        self.db1name = self.locname + ".txt"
        os.chdir("/users/ugrad/biswasma/Desktop/CN-Data-Fabric-Provider/GCS")
        self.f1 = open(self.db1name, "w")
        self.f1.write('[]')
        self.f1.close()

        for i in range(2, int(clients) + 1):
            self.db2name = self.locname + str(i) + ".txt"
            os.chdir("/users/ugrad/biswasma/Desktop/CN-Data-Fabric-Provider/GCS")
            self.f2 = open(self.db2name, "w")
            self.f2.write('[]')
            self.f2.close()

    # Function to update the global db as and when blocks are created
    def globalcdb(self, key):
        multithreadServer('rasp-008', 33333, key).listen()
        # TO DO - add code for decentralised server socket implementation with broadcast messages to invoke UAV's
        pass
