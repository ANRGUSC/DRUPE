# ** Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
# **     contributor: Quynh Nguyen, Bhaskar Krishnamachari
# **     Read license file in main directory for more details

# Instructions copied from - https://hub.docker.com/_/python/
FROM ubuntu:16.04

# Install required libraries
RUN apt-get update
RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev
RUN apt-get -yqq install python3-pip python3-dev
RUN pip3 install --upgrade pip
RUN apt-get install -y openssh-server mongodb sshpass nano virtualenv supervisor

# Install required python libraries
RUN pip install cryptography
ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# Authentication
RUN echo 'root:apac20!7' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Prepare MongoDB
RUN mkdir -p /mongodb/data
RUN mkdir -p /mongodb/log
RUN mkdir -p /root/networkprofiling
ADD central_mongod /root/networkprofiling/central_mongod


# Prepare network profiling code
ADD central_input /root/networkprofiling/central_input
ADD central_copy_nodes /root/networkprofiling/central_copy_nodes
ADD central_query_statistics.py /root/networkprofiling/central_query_statistics.py
ADD central_scheduler.py /root/networkprofiling/central_scheduler.py
RUN mkdir -p /root/networkprofiling/scheduling
RUN mkdir -p /root/networkprofiling/parameters

# Running docker
ADD start.sh /root/networkprofiling/start.sh
RUN chmod +x /root/networkprofiling/start.sh
WORKDIR /root/networkprofiling
# tell the port number the container should expose
EXPOSE 22
CMD ["./start.sh"]


