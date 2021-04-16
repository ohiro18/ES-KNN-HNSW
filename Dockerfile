FROM python:3.8-slim
  
RUN pip install -U pip
RUN pip install elasticsearch
RUN pip install flask

RUN mkdir -p /home/flask/static

COPY ./app/ /home/
WORKDIR /home/flask
CMD ["python", "-u", "app.py"]