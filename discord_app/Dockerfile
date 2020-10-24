FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/app
ENV HOME=/usr/app
WORKDIR $HOME

RUN apt update && apt upgrade -y

ADD requirements.txt $HOME
RUN pip install -r requirements.txt