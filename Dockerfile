FROM python:3.6-alpine

RUN adduser -D tuwbroker
WORKDIR /home/tuwbroker

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY openservicebroker.py start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP openservicebroker.py

RUN chown -R tuwbroker:tuwbroker ./
USER tuwbroker

EXPOSE 5000
ENTRYPOINT ["./start.sh"]