FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV TZ=Asia/Tokyo

RUN mkdir -p /usr/mocrat/app
ENV HOME=/usr/mocrat/app
WORKDIR $HOME

RUN apt update && apt upgrade -y

ADD requirements.txt $HOME
RUN pip install -r requirements.txt