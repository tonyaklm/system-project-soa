FROM python:3.8-slim

WORKDIR .

COPY statistics-service/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip
RUN apt-get -y update; apt-get -y install curl


COPY statistics-service/src/ /
COPY common/ /common/

CMD ["python", "main.py"]