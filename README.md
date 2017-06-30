Dispersed-Computing-Profiler (DRUPE)
====================================


CENTRAL NETWORK PROFILER
-------------------------

1. Description: automatically scheduling and logs communication information of all links betweet nodes in the network, which gives the quaratic regression parameters of each link representing the corresponding communication cost. These results are required in the next step for HEFT algorithm.

2. Input

- File central.txt stores credential information of the central node

CENTRAL IP      USERNAME   PASSWORD
----------      --------   --------
107.170.77.194  apac       apac20!7

- File nodes.txt stores credential information of the nodes information

TAG      NODE (username@IP)     REGION
-----    --------               ------
node1    apac@104.131.111.58    NYC
node2    apac@139.59.58.153     BLR
node3    apac@207.154.243.148   FRA

- File link list.txt stores the the links between nodes required to log the communication

SOURCE(TAG)    DESTINATION(TAG)
-----------    ----------------
node1          node2
node1          node3
node2          node1
node2          node3
node3          node1
node3          node2

3. Output: all quadratic regression parameters are stored in the local MongoDB on the central node.

4. Userguide (Non-dockerized version):

    * At the central network profiler:
        * run the command ./central init to install required libraries
        * inside the folder central input add information about the nodes and the links.
        * python3 central scheduler.py to generate the scheduling files for each node, prepare the central database and collection, copy the scheduling information and network scripts for each node in the node list and schedule updating the central database every 10th minute.

    * At the droplets:
        * The central network profiler copied all required scheduling files and network scripts to the folder online profiler in each droplet.
        * run the command ./droplet init to install required libraries
        * run the command python3 automate droplet.py to generate files with different sizes to prepare for the logging measurements, generate the droplet database, schedule logging measurement every minute and logging regression every 10th minute.

5. Userguide (Dockerized version)

    * At the docker_online_profiler folder:
        * Modify input in folder central_input (nodes.txt, link_list.txt) of central_network_profiler and upload_docker_network accordingly (IP, PASSWORD, REG, link_list)
        * Run: ./upload_docker_network to upload codes to all the nodes and the central
        * Example run: Scheduler IP0, and other droplets IP1, IP2, IP3

    * At the droplets, inside the droplet_network_profiler:
        * Build the docker: docker build -t droplet_network_profiler .
        * Run the containers:

        docker run --rm --name droplet_network_profiler -t -i -e DOCKER_HOST=IP1 -p 5100:22 -P droplet_network_profiler
        docker run --rm --name droplet_network_profiler -t -i -e DOCKER_HOST=IP2 -p 5100:22 -P droplet_network_profiler
        docker run --rm --name droplet_network_profiler -t -i -e DOCKER_HOST=IP3 -p 5100:22 -P droplet_network_profiler

    * At the central network profiler (IP0):
        * Build the docker: docker build -t central_network_profiler .
        * Run the container:

        docker run --rm --name  central_network_profiler -i -t -e DOCKER_HOST=IP0 -p 5100:22 -P central_network_profiler

RESOURCE PROFILER
-------------------------





