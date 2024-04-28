FROM python:3.8-slim

WORKDIR .

COPY social-media/requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN apt-get -y update; apt-get -y install g++
RUN apt-get -y update; apt-get -y install curl

RUN pip install --upgrade setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt



EXPOSE 8000

COPY social-media/src/ /
COPY common/ /common/

CMD ["python", "main.py"]