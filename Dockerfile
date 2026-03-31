FROM python:3.14

RUN mkdir /var/app
WORKDIR /var/app
COPY start.py app.py requirements.txt /var/app
RUN apt-get update && apt-get install -y \
    uwsgi \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt

CMD ["uwsgi", "--master","--http-socket", "0.0.0.0:33332", "--wsgi-file", "start.py"]

EXPOSE 33332

