import sys
sys.dont_write_bytecode = True

from GCS.gcs import *

# Program to get the Ground Control Station up and running
iarray = sys.argv[1:]
i = iarray[0]

k = input("Enter the numeric decryption key: ")

while k.isdigit() == False:
    k = input("Enter the NUMERIC DECRYPTION KEY!: ")

k = int(k)

groundcontrolstation = GCS(i)
groundcontrolstation.globalcdb(k)
