from Blockchain.blockchain import *
from Network.server import *
import os

# Class containing member functions and variables for the Ground Control Station(GCS)
class GCS(Blockchain, multithreadServer):

    # Constructor function to declare and initialise all member variables being used alongside calling the superclass
    def __init__(self):
        Blockchain.__init__(self, 0, 250)
        
        # Creating a database for the blockchain
        self.dbname = self.locname + ".txt"
        os.chdir("/users/ugrad/biswasma/Desktop/CN-Data-Fabric-Provider/GCS")
        self.f = open(self.dbname, "w")
        self.f.write('[]')
        self.f.close()

    # Function to update the global db as and when blocks are created
    def globalcdb(self):
        multithreadServer('rasp-008',33333).listen()
        # TO DO - add code for decentralised server socket implementation with broadcast messages to invoke UAV's
        pass
