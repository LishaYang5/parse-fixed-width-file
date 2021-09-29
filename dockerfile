FROM python:3.8

COPY app .
WORKDIR /app

VOLUME [ "/dataVolumeContainer1","/dataVolumeContainer2" ]
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["main.py"]
