FROM python:3.8-slim-buster
WORKDIR /Mini_Capstone_project
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python" ] 
CMD ["server.py"]

EXPOSE 8000
