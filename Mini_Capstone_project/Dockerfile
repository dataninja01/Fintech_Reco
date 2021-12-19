FROM python:3.8
RUN apt-get update && \
apt-get install -y python3-pip python3-dev git && \
apt-get -y upgrade
COPY . /Mini_Capstone_project
WORKDIR /Mini_Capstone_project
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ] 
CMD ["sentiment_analysis.py", "server.py", "request.py"]

EXPOSE 5000