import sys
sys.dont_write_bytecode = True

from UAV.uav import *
from keyboard import *
import sys

# Program to simulate various test cases on the UAV and the Blockchain

# Function to write to the localdb when disconnected from the global db
def localwriteFunc(p1, UAVi, i):
    while True:
        try:
            # Simluation of test cases where the UAV disconnects from the GCS
            p1 = UAVi.localBuff(i)
            p1 = 75
            UAVi = UAV(p1)

        except KeyboardInterrupt:
            p1 = 75
            globalwriteFunc(p1)


# Function to write to the global db
def globalwriteFunc(p1):
    while True:
        try:
            # Simulation of test cases where the UAV is connected to the GCS
            UAVi = UAV(p1)
            p1 = UAVi.globalcdb()

        except KeyboardInterrupt:
            p1 = 75
            localwriteFunc(p1, UAVi, i)


try:
    # Declaration of proof for the first block within the blockchain
    i = sys.argv[1:]
    p1 = 1
    globalwriteFunc(p1)

except:
    pass
