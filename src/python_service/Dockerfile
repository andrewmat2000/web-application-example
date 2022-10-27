FROM python:3.10-alpine

RUN adduser -D python

RUN apk add --update python3 py3-pip

# USER python

WORKDIR /opt/python_service
COPY ./ /opt/python_service

# COPY ./ ~/python_service

#RUN pip install Flask

RUN chmod +x ./start.sh
RUN python3 -m venv venv
RUN chmod +x venv/bin/pip
RUN venv/bin/python3 -m pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt


CMD './start.sh'