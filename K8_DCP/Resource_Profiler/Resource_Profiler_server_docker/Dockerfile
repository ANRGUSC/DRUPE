FROM python:2
RUN pip install flask\
&& pip install psutil

RUN mkdir server

EXPOSE 49155:5000

COPY server.py /server

CMD	["python","server/server.py"] 

