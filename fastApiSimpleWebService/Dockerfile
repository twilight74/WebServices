FROM python:3.9

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip3 install -r requirments.txt

COPY . .



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000 ", "--no-date-header", "--no-server-header"]

