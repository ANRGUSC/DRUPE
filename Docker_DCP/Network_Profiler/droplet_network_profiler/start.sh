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
my_ip=$DOCKER_HOST

./droplet_generate_random_files $my_ip

echo 'Step 3 -  Prepare MongoDB database, Automatically run measurement and regression script'

python3 automate_droplet.py $my_ip







