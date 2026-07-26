FROM python:3.14.3-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask mysql-connector-python

EXPOSE 5000

CMD ["python", "app.py"]
