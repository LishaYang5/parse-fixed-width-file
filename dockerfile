FROM python:3.8-bullseye

WORKDIR /app
COPY app .


VOLUME [ "/app","/app" ]
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["main.py"]
