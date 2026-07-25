FROM python:3.14.3-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask mysql-connector-python

ENV MYSQL_HOST=database \
    MYSQL_USER=root \
    MYSQL_PASSWORD=kali \
    MYSQL_DATABASE=tailstore

EXPOSE 5000

CMD ["python", "app.py"]
