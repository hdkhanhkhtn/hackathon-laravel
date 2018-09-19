FROM python:3.4-slim
ENV PYTHONUNBUFFERED 1

MAINTAINER HDK "hdkhanh.khtn@gmail.com"

# install scrapy
RUN apt-get update && \
    apt-get install --assume-yes --no-install-recommends \
        gcc \
        libffi-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        python-pip \
        python-dev \
        postgresql-client \
        zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /workspace
WORKDIR /workspace
ADD requirements.txt /workspace/
RUN pip install -r requirements.txt
ADD . /workspace/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
ENV TZ UTC

