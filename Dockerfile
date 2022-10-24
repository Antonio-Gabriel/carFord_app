# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_APP main.py

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y git build-essential cmake clang libssl-dev
RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip --no-cache-dir install -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

entrypoint "/entrypoint.sh"

CMD ["python3", "-m", "flask", "run", "--host=127.0.0.1"]
