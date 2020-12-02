FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV TZ=Asia/Tokyo

RUN mkdir -p /usr/app
ENV HOME=/usr/app
WORKDIR $HOME

RUN useradd ubuntu
RUN apt update && apt upgrade -y
RUN apt install wine -y

ADD requirements.txt $HOME
RUN pip install -r requirements.txt
