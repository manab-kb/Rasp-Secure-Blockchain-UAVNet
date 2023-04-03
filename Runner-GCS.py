import sys
sys.dont_write_bytecode = True

from GCS.gcs import *

# Program to get the Ground Control Station up and running
groundcontrolstation = GCS()
groundcontrolstation.globalcdb()
