FROM python:3.7-alpine
WORKDIR /app
COPY app .

VOLUME [ "/app" ]
EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["main.py"]