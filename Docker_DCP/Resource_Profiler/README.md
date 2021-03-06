1.Introduction

This Resource Profiler is running inside docker containers. It will get system utilization from node 1, node 2 and node 3. Then these information will be sent to home node and stored into mongoDB. 

The information includes: IP address of each node, cpu utilization of each node, memory utilization of each node, and the latest update time.

2. User Guide

It consists of the following steps:

2.1 For working nodes(node1, node2 and node3):
	(1) copy the Resource_Profiler_server_docker/ folder to each working node using scp.
	(2) in each node, type:
		docker build -t server .
		docker run -d -p 49155:5000 server

2.2 For scheduler node:
	(1) copy Resource_Profiler_control_docker/ folder to home node using scp.
	(2) if a node’s IP address changes, just update the Resource_Profiler_control_docker/control_file/ip_path file (optional, see 	section 3 below for detail)
	(3) find central_network_profiler container by typing docker inspect CONTAINER ID. Get the IP address.
	(4) type mongo IP and then go inside mongo shell. And type:
		use DBNAME
			db.createUser({
				user: 'USERNAME',
				pwd: 'PASSWORD',
				roles: [{ role: 'readWrite', db:'DBNAME'}]
			}}
	(3) inside Resource_Profiler_control_docker/ folder, type:
		docker build -t control .
		docker run control

3. Structure

	Resource_Profiler_server_docker/
		server.py
		DOckerfile

	Resource_Profiler_control_docker/
		/Dockerfile
		/control_file/
			insert_to_container.py
			read_info.py
			read_info.pyc
			job.py
			ip_path

note: the content of ip_path are several lines of working nodes’ IP address. So if a node’s IP address is changed, make sure to update the ip_path file.
