FROM python:3.8-slim-buster

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip3 install -r requirments.txt

COPY . .



CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--no-server-header","--no-date-header"]

