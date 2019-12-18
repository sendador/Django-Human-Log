FROM python:3.8

#It's doesn't allow python to buffer the outputs. Just print them directly
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#It's create empty folder on our docker image and then switch it to default. Next it copy from our local machine to app folder in img
RUN mkdir /hlog
WORKDIR /hlog
COPY ./hlog /hlog