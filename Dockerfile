FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir orm
WORKDIR /orm


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .