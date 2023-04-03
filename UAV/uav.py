import sys
sys.dont_write_bytecode = True

from Blockchain.blockchain import *
from random import *
from math import *
import os
from Network.client import *
from threading import *

# Class containing member functions and variables for each individual UAV (Unmanned Aerial Vehicle - Drone)
class UAV(Blockchain, client):

    # Constructor function to declare and initialise all member variables being used alongside calling the superclass
    def __init__(self, proof):
        Blockchain.__init__(self, proof, 250)
        # Initializing client class with hostname and port number
        client.__init__(self, 'rasp-008', 33333)
        # self.lastBlock = self.bchain[-1] Temporary fix

        # Declaring and initializing variables to be used to compute proof for POW
        templat = self.initLat
        templong = self.initLong
        proof = proof
        dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))

        # Producing a random variable out of 4 choices to determine the direction amongst 4-axis in which the drone will navigate in order to cover all possible areas from the initial coordinates
        choice = randint(0,3)
        if choice == 0:
            # For each choice, checking if POW is completed. If not, incremental changes in coordinates are made and are tested again.
            while self.poW(dist) == False:
                templat += 0.00500
                templong += 0.00500
                proof += 1
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        if choice == 1:
            while self.poW(dist) == False:
                templat -= 0.00500
                templong += 0.00500
                proof += 2
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        if choice == 2:
            while self.poW(dist) == False:
                templat -= 0.00500
                templong -= 0.00500
                proof += 3
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        if choice == 3:
            while self.poW(dist) == False:
                templat += 0.00500
                templong -= 0.00500
                proof += 4
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))

        # Finding hashvalue for the block to be added and calling the functions to create and validate the block before being added into the blockchain
        if len(self.bchain) > 1:
            Blockchain.__init__(self, proof, 250)
            print("@log: Block Generated")
            self.createBlock()

        if len(self.bchain) <= 1:
            Blockchain.__init__(self, proof, 250)
            print("@log: Block Generated")
            self.createBlock()

        # Thread(target = self.validate, args = ())
        self.validate()
        print("@log: Block Validated")

    def globalcdb(self):
        self.serverConn(self.bchain)
        return self.proof
        # TO DO - add client socket code to communicate with other client sockets (decentralised) without the gcs and also with the gcs
        # Also add code to switch to local buffers only when UAV is disconnected from blockchain and match and update central blockchain db once connection is reestablished
        # Ensure GBN / SR and Timeouts are used to make the client code reliable
        # Also ensure UAV continues to run after one unit of proof has been generated (reset statistics)
        # Finally, also include coordinates for the drone in each block communication such that the location of the drone can be traced at any given point in time (useful when drone disconnects to find last active location)

    # Function used to switch creating blocks into the local buffer of each UAV when it disconnects from the central DB / Blockchain network
    def localBuff(self, index):
        # Creating a local db for the UAV if it already doesnt exist
        # index = self.lastBlock['index']
        # index = 1  #Temporary fix
        dirname = "UAV" + str(index)
        os.chdir("/users/ugrad/biswasma/Desktop/Rasp-Secure-Blockchain-UAVNet/UAV")
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        os.chdir(dirname)

        # Continuing to write to the local db unless connection is established
        localf = open("localBChain.txt" , "w")
        localf.write(str(self.bchain))
