import sys
sys.dont_write_bytecode = True

# from geopy import * - TEMPORARY FIX UNTIL API CALLS THROUGH PROXY ARE DISCOVERED
from datetime import *
from hashlib import *
from json import *
import ast
import os

# Class containing member functions and variables for the blockchain
class Blockchain:

    # Constructor function to declare and initialize all member variables being used
    def __init__(self, proof, powlen, initLat = 53.344250, initLong = -6.262410):
        if proof == 0:
            # Creating an empty blockchain
            self.bchain = []
        elif proof == 75:
            # Merges the largest available chain from the local buffers of each UAV
            templocaldata = []
            dirname = "/users/ugrad/biswasma/Desktop/Rasp-Secure-Blockchain-UAVNet/UAV/"
            for filename in os.listdir(dirname):
                if filename != 'uav.py':
                    localdirname = os.path.join(dirname, filename)
                    os.chdir(localdirname)
                    localfile = open("localBChain.txt", "r")
                    templocaldata.append(localfile.read())
                    localfile.close()
            templocaldata.sort()
            localdata = templocaldata[-1]
            self.bchain = ast.literal_eval(localdata)
        else:
            # Opens the most recent copy of the blockchain in the Global DB
            file = open("/users/ugrad/biswasma/Desktop/Rasp-Secure-Blockchain-UAVNet/GCS/College Green.txt", "r")
            data = file.read()
            file.close()
            # ADD CODE TO FIX RACE CONDITIONS
            self.bchain = ast.literal_eval(data)

        # Tuple for coordinates from location coordinates entered by the user / default values
        self.initLat = initLat
        self.initLong = initLong
        self.coord = (self.initLat, self.initLong)

        # Declaring and initialising variables for proof, hash, prevhash and powlen
        self.proof = proof
        self.prevhash = 0
        self.powlen = powlen

        # Determining name of location from coordinates - to name the centralised database
        # self.geoloc = Nominatim(user_agent="blockchain_uavnet") - TEMPORARY FIX UNTIL API CALLS THROUGH PROXY ARE DISCOVERED
        # self.loc = str(self.geoloc.reverse(self.coord)) - TEMPORARY FIX UNTIL API CALLS THROUGH PROXY ARE DISCOVERED
        # self.locname = self.loc[3:16] - TEMPORARY FIX UNTIL API CALLS THROUGH PROXY ARE DISCOVERED
        self.locname = "College Green"

    # Function to create and append a new block
    def createBlock(self):
        # New block is based on proof from the current UAV and hash values of the prev block
        if len(self.bchain) == 0:
            self.prevHash = 0
        else:
            tempblock = self.bchain[-1]
            self.prevHash = self.hashValue(tempblock)
        self.newBlock = {'index' : len(self.bchain) + 1, 'prevHash' : self.prevHash, 'proof' : self.proof, 'timestamp' : str(datetime.now())}
        self.bchain.append(self.newBlock)

    # Function to calculate the hashvalue for the block
    def hashValue(self, dict):
        encodedBlock = dumps(dict).encode()
        hashVal = md5(encodedBlock).hexdigest()
        return hashVal

    # Function for Proof Of Work (POW)
    def poW(self, powcomp):
        # checking if the area covered by the UAV matches the defined area to be covered by the GCS
        if powcomp < self.powlen:
            # print("@log: POW match failed: Covered area lesser than defined area.")
            return False
        else:
            return True

    # Function to validate each transaction of data within the blockchain
    def validate(self):
        if len(self.bchain) == 1:
            pass

        blockind = 1

        # Checking if block indices and hash values are as needed
        while blockind < len(self.bchain):
            block1 = self.bchain[blockind-1]
            block2 = self.bchain[blockind]

            if self.hashValue(block1) != block2['prevHash']:
                print("@log: hashvalue mismatch.")

            else:
                blockind+=1
