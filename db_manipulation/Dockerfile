FROM python:3.10.12-slim-bullseye

RUN apt update && apt install -y libpq-dev gcc

COPY db_manipulation/requirements.txt /requirements.txt

RUN pip install -r requirements.txt
