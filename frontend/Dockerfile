FROM python:3.7-alpine

COPY . /app
RUN true && apk add \
     gcc \
     linux-headers \
     musl-dev \
     && true
RUN pip install --no-cache-dir -r /app/requirements.txt 
EXPOSE 80
CMD python /app/app.py