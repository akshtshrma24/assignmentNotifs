FROM python:3.10.1-slim-buster

ENV TZ="America/Los_Angeles"

WORKDIR /canvas

EXPOSE 5000

RUN pip3 install --upgrade pip

RUN pip install requests

COPY /data/* ./
COPY /scraper/* ./
COPY /util/* ./

#Pinging Google's Public DNS Server
CMD ["python3", "scraper.py"]