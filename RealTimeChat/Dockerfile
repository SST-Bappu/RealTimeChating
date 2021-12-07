FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /chat
COPY requirements.txt /chat/requirements.txt
RUN pip install -r requirements.txt
COPY . /chat

