from UAV.uav import *
from keyboard import *

# Program to simulate various test cases on the UAV and the Blockchain

# Function to write to the localdb when disconnected from the global db
def localwriteFunc(p1, UAV1):
    while True:
        try:
            # Simluation of test cases where the UAV disconnects from the GCS
            p1 = UAV1.localBuff()
            p1 = 75
            UAV1 = UAV(p1)

        except KeyboardInterrupt:
            p1 = 75
            globalwriteFunc(p1)


# Function to write to the global db
def globalwriteFunc(p1):
    while True:
        try:
            # Simulation of test cases where the UAV is connected to the GCS
            UAV1 = UAV(p1)        
            p1 = UAV1.globalcdb()
        
        except KeyboardInterrupt:
            p1 = 75
            localwriteFunc(p1, UAV1)


try:
    # Declaration of proof for the first block within the blockchain
    p1 = 1
    globalwriteFunc(p1)

except:
    pass
