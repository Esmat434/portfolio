FROM python:3.10-alpine

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /src/app

COPY requirements.txt .

RUN apk add --no-cache \
    build-base \
    mariadb-client \
    mariadb-dev \
    libjpeg-turbo-dev \
    zlib-dev 

RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

COPY docker_scripts/entrypoint.sh /entrypoint.sh 

RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]