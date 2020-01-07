FROM python:3.9.0a2-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /hlog
WORKDIR /hlog
COPY requirements.txt /hlog/
COPY . /hlog/
RUN pip install -r requirements.txt
COPY . .