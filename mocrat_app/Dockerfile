FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/mocrat/app
ENV HOME=/usr/mocrat/app
WORKDIR $HOME

RUN apt update && apt upgrade -y

COPY mocrat_cron /etc/cron.d/mocrat_cron
RUN chmod 0644 /etc/cron.d/mocrat_cron
RUN crontab /etc/cron.d/mocrat_cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

ADD requirements.txt $HOME
RUN pip install -r requirements.txt