FROM python:3.10.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt 
RUN pip install -r requirements.txt 

COPY . .