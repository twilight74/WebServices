FROM python:3.9

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip3 install --no-cache-dir --upgrade -r requirments.txt

COPY . .




CMD [ "python", "-m","uvicorn", "djangoSimpleWebService.asgi:application", "--host", "0.0.0.0", "--port", "7000", "--no-server-header", "--no-date-header"]