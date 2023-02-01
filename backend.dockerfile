# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
FROM python:3.9-slim-bullseye

# set environment variables
ENV TZ=Asia/Bangkok
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# set working directory
WORKDIR ./app

# copy dependencies
COPY requirements.txt .

# install FreeTDS and dependencies
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

# # populate "ocbcinst.ini"
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

# install pyodbc (and, optionally, sqlalchemy)
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org pyodbc==4.0.32

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /app/