# Version: 0.0.1

# Pull base image.
FROM python:2.7-slim

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
        zlib1g-dev && \
        default-libmysqlclient-dev && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip && \
    pip install --upgrade \
        setuptools \
        wheel && \
    pip install --upgrade scrapy && \
    pip install --upgrade SQLAlchemy

RUN mkdir -p /workspace

# Define working directory.
WORKDIR /workspace

ADD requirements.txt /workspace/
RUN pip install -r requirements.txt

ENV TZ UTC

