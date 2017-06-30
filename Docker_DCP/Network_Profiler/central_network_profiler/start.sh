#!/bin/bash
: '
    ** Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
    **     contributor: Quynh Nguyen, Bhaskar Krishnamachari
    **     Read license file in main directory for more details
'

service ssh start

echo 'Installing and starting mongodb'
./central_mongod start

echo 'Automatically run the central network scheduler'
python3 central_scheduler.py




