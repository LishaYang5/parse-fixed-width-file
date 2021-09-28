FROM python:3.7-alpine
WORKDIR /app
COPY app .

RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["main.py"]