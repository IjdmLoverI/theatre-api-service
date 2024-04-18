FROM python:3.11-alpine
LABEL maintainer="kbuchinskiywork@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
