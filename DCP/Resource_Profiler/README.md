1.Introduction

This Resource Profiler will get system utilization from node 1, node 2 and node 3. Then these information will be sent to home node and stored into mongoDB. 

The information includes: IP address of each node, cpu utilization of each node, memory utilization of each node, and the latest update time.

2. User Guide

It consists of the following steps:

2.1 For working nodes(node1, node2 and node3):
	(1) copy the Resource_Profiler_server/ folder to each working node using scp.
	(2) in each node, type:
		python2 Resource_Profiler_server/install_package.py

2.2 For scheduler node:
	(1) copy Resource_Profiler_control/ folder to home node using scp.
	(2) if a node’s IP address changes, just update the Resource_Profiler_control/ip_path file (optional, see 	section 3 below for detail)
	(3) inside Resource_Profiler_control/ folder, type:
		python2 install_package.py
 		python2 jobs.py (if you want to run in backend, type: python2 jobs.py & and then close the  terminal)

3. Structure

	Resource_Profiler_server/
		server.py
		install_package.py

	Resource_Profiler_control/
		insert_to_mongo.py
		read_info.py
		read_info.pyc
		install_package.py
		jobs.py
		ip_path

note: the content of ip_path are several lines of working nodes’ IP address. So if a node’s IP address is changed, make sure to update the ip_path file.
