#!/bin/bash
: '
    ** Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
    **     contributor: Quynh Nguyen, Bhaskar Krishnamachari
    **     Read license file in main directory for more details
'

service ssh start

echo '---------------Step 1 - Installing and starting mongodb----------------'
./droplet_mongod start

echo '---------------Step 2 - Generating random test files--------------------'
# my_ip=$SELF_IP
# echo $my_ip
# The SELF_IP environment variable contains the ip of the k8 service
./droplet_generate_random_files $SELF_IP

echo 'Step 3 -  Prepare MongoDB database, Automatically run measurement and regression script'

python3 -u automate_droplet.py $SELF_IP







