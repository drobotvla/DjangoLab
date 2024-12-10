FROM python:3.10.12-slim-bullseye

RUN apt update && apt install -y libpq-dev gcc

COPY supply_department /supply_department

WORKDIR /supply_department

RUN pip install -r requirements.txt

CMD ["gunicorn", "--workers", "3",  "--bind", "0.0.0.0:8000", "supply_department.wsgi:application"]
