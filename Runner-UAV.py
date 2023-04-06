import sys
sys.dont_write_bytecode = True

from UAV.uav import *
from keyboard import *
import sys
import time

# Program to simulate various test cases on the UAV and the Blockchain

# Function to write to the localdb when disconnected from the global db
def localwriteFunc(p1, UAVi, i):
    while True:
        try:
            # Simluation of test cases where the UAV disconnects from the GCS
            p1 = UAVi.localBuff(i)
            p1 = 75
            UAVi = UAV(p1, i)

        except KeyboardInterrupt:
            p1 = 75
            globalwriteFunc(p1, i)


# Function to write to the global db
def globalwriteFunc(p1, i):
    while True:
        try:
            # Simulation of test cases where the UAV is connected to the GCS
            UAVi = UAV(p1, i)
            p1 = UAVi.globalcdb(i, dk)

        except KeyboardInterrupt:
            p1 = 75
            localwriteFunc(p1, UAVi, i)


try:
    # Declaration of proof for the first block within the blockchain
    iarray = sys.argv[1:]
    i = iarray[0]
    p1 = 1

    dk = input("Enter the encryption key: ")

    while dk.isdigit() == False:
        dk = input("Enter the NUMERIC encryption key: ")

    dk = int(dk)
    globalwriteFunc(p1, i)

except:
    pass
