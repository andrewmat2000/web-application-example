FROM python:3.10-alpine

WORKDIR /opt/python_service
COPY ./ /opt/python_service

RUN chmod +x ./start.sh
RUN python3 -m venv venv
RUN chmod +x venv/bin/pip
RUN venv/bin/python3 -m pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

CMD './start.sh'