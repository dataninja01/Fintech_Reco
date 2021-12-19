FROM python:3.8
RUN apt-get update && \
apt-get install -y python3-pip python3-dev git && \
apt-get -y upgrade
RUN cd /opt && \
git clone https://github.com/dataninja01/Fintech_Reco.git && \
cd Fintech_Reco && \
cd Mini_Capstone_project && \
pip3 install -r requirements.txt
ENTRYPOINT [ "python" ] 
CMD ["sentiment_analysis.py", "server.py", "request.py"]

EXPOSE 5000