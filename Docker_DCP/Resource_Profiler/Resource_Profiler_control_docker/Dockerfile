FROM python:2
RUN pip install requests\
&& pip install pymongo

RUN mkdir control



COPY control_file/ /control

CMD	["python","control/job.py"] 

