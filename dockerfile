FROM python:3.7-alpine
WORKDIR /app
COPY app .

RUN pip install --upgrade pip
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

RUN python -m unittest -v

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["testParser.py"]