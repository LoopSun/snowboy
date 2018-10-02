FROM python:3.5.6-alpine3.8

COPY ./src /app/
RUN pip install -r /app/main/requirement
WORKDIR /app/

EXPOSE 5000

ENTRYPOINT ["sh", "/app/start.sh"]
