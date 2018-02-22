FROM ubuntu:latest

WORKDIR /app
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
COPY distrib/ ./
RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python", "quotable.py"]
