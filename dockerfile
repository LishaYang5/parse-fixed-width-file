FROM python:3.8.8
ADD . /app
WORKDIR /app
COPY app .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["parser.py", "/app/parser.py"]