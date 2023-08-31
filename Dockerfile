# Author: Sanjib Kumar Paul
# Created Date: 30-08-2023

FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /asset_management
RUN mkdir /var/log/asset_management
RUN touch /var/log/asset_management/asset_management.log

COPY requirements.txt /asset_management/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /asset_management/
EXPOSE 3000