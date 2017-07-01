'''
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributor: Jiatong Wang, Bhaskar Krishnamachari
 *     Read license file in main directory for more details
'''

import paramiko
import time, os

node1="IP1"
node2="IP2"
node3="IP3"

def control_nodeIP1():

    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh1.connect(node1 , username="USERNAME", password="PASSWORD")
    print "node1 connect successfully!"
    ssh1.exec_command('python2 mongo_script/install_package.py')
    print "dependency install successfully!"
    ssh1.exec_command('python2 mongo_script/server.py')
    print "node1 listen at port 5000\n"

def control_nodeIP2():

    ssh2 = paramiko.SSHClient()
    ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh2.connect(node2 , username="USERNAME", password="PASSWORD")
    print "node2 connect successfully!"
    ssh2.exec_command('python2 mongo_script/install_package.py')
    print "dependency install successfully!"
    ssh2.exec_command('python2 mongo_script/server.py') 
    print "node2 listen at port 5000\n"

def control_nodeIP2():

    ssh3 = paramiko.SSHClient()
    ssh3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh3.connect(node2 , username="USERNAME", password="PASSWORD")
    print "node3 connect successfully!\n"
    ssh3.exec_command('python2 mongo_script/install_package.py')
    print "dependency install successfully!"
    ssh3.exec_command('python2 mongo_script/server.py')
    print "node3 listen at port 5000\n"

def re_exe(cmd, inc = 60):
    while True:
        os.system(cmd)
        time.sleep(inc)


if __name__=="__main__":
    control_nodeIP1()
    control_nodeIP2()
    control_nodeIP3()
    re_exe("python2 insert_to_mongo.py ip_path", 60)
