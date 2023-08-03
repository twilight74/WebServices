FROM python:3.8-slim-buster

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip3 install -r requirments.txt

COPY . .


CMD ["python3","-m", "nose2"]

