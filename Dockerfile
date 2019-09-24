FROM python:3
RUN apt-get update -y && apt-get install -y python3-pip python3-dev
COPY . /app
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
EXPOSE 5000
EXPOSE 8081
CMD ["python", "-u" ,"main.py",  "--host", "0.0.0.0"]