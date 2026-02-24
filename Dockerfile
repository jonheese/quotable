FROM ubuntu:latest

WORKDIR /app
RUN apt-get update
RUN apt-get install -y python3-pip
COPY distrib/ ./
RUN pip install -r requirements.txt --break-system-packages

EXPOSE 80
ENTRYPOINT ["python3", "quotable.py"]
