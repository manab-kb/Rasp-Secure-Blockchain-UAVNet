# Rasp-Secure-Blockchain-UAVNet
A repository containing an implementation of a secure blockchain based decentralized and distributed network, targeted towards improving unmanned vehicular communications (UAV's) in conflict zone scenarios.

# How to run ?
1. Clone the **main** branch of this repository to your local machine.
2. Make changes to the path present in the following lines within the following files (to match the directory within your local machine where the repository is cloned):

        a. Line 16 and 21 : Blockchain/blockchain.py
    
        b. Line 14 - GCS/gcs.py
     
        c. Line 30 - Network/server.py

        d. Line 82 - UAV/uav.py
3. `pip install -r requirements.txt`  - to install all the requirements present within the requirements.txt file.
4. Depending on the OS on which the program is being run; run the following commands (in order) in a terminal window within the cloned repository:

    1. (a) `python .\Runner-GCS.py` or `python Runner-GCS.py` - **Windows based systems**.
    
       (b) `python3 Runner-GCS.py` - **Linux based systems**

    2. (a) `python .\Runner-UAV.py` or `python Runner-UAV.py` - **Windows based systems** (Run this command in a new terminal window)
        
       (b) `python3 Runner-UAV.py` - **Linux based systems** (Run this command in a new terminal window)

# Test Cases
1. **Ideal conditions** - To test the blockchain network under ideal conditions, follow the steps mentioned in the section ***How To Run*** (above). You should see a file named **College Green.txt** being generated and populated, located within the **GCS** subdirectory of your cloned project.
2. **Failure of UAV's** - To test the blockchain network in a case where a UAV has been disconnected from the network, follow the below mentioned steps:

    1. Follow the steps mentioned in the section ***How To Run*** (above).
    2. On the terminal window containing logs from the command **Runner-UAV.py**, press `Ctrl + C`.
    3. A subdirectory named **UAV1** should be generated within the **UAV** subdirectory of your cloned project. The newly generated subdirectory should also contain a file named **localBChain.txt** which should be populated with all the contents of the blockchain and should continue to be populated until further reconnection of the UAV to the GCS.
    4. To reconnect the UAV to the GCS and blockchain network, navigate back to the terminal window mentioned in *Step ii* of this section. On this window, press `Ctrl + C` (yet again) to reconnect the UAV back to the GCS. You should observe that the file **College Green.txt** continues to be updated as and when the UAV is reconnected.
3. **Disconnection of the GCS** - To test the blockchain network in a case where the GCS has been disconnected from the blockchain, follow the below mentioned steps:

    1. Follow the steps mentioned in the section ***How To Run*** (above).
    2. On the terminal window containing logs from the command **Runner-GCS.py**, press `Ctrl+C`.
    3. On the terminal window containing logs from the command **Runner-UAV.py**, press `Ctrl+C`.
    4. You should observe that the file **localBChain.txt** (mentioned under *Step iii* of *Section 2*) would be populated with all the contents of the blockchain and would continue to be updated unless acted upon the GCS otherwise.
    5. To reconnect the GCS back to the blockchain network, run the commands mentioned under *Step 4.i*, present under the section ***How To Run*** (above), in a new terminal window.
    6. On the terminal window mentioned in *Step iii* of this section, press `Ctrl+C` yet again, and you should see all files being populated as expected in an ideal condition.

4. **Presence of multiple UAVs** - to test the presence of multiple UAVs within the blockchain network, simply follow all the steps above containing the file **Runner-UAV.py** 'n' number of times, where n is the number of UAVs that you would like to create.

# Note
This program involves the use of **OS** libraries, which create and modify files within the project directory. This might result in the need for access to certain permissions or RBAC modes. Hence, we recommend that you clone this project to a local directory on your machine (such as **Desktop**) which would not additional permissions to create and modify files.

# Contributing to CN-Data-Fabric-Provider
Hello and welcome! We are so glad that you are interested in contributing to CN Data Fabric Provider!
We only have a couple of rules and we hope you enjoy the process :)

## Contributing Rules
1. Don't move or delete any files. Only modify them.

## Contributing Process
1. Fork the repository
2. Clone your forked repository to your computer
3. Head to the issues tab and look for an issue that you like.
4. Once you have decided what issue to work on, give it a shot!
5. Once done, push the code to your forked repository.
6. Head to the Pull Requests tab and click on "Create New Pull Request"
7. On the left of the arrow should be this repo and on the right should be yours.
8. Add a small description to the Pull Request describing what you've done.
9. Mention what Issue you have worked on. If the issue number is #3, you can mention "Closes #3" in the Pull Request description.
10. Submit Pull Request

It's that easy! We hope you enjoy contributing to our repository. Don't hesitate to contact any of the maintainers about any problems!
