FROM python:3.8
RUN apt-get update && \
apt-get install -y python3-pip python3-dev git && \
apt-get -y upgrade
RUN cd /opt && \
git clone https://github.com/dataninja01/Fintech_Reco.git && \
cd Fintech_Reco && \
cd Mini_Capstone_project && \
pip3 install -r requirements.txt
RUN python3 /opt/Mini_Capstone_project/sentiment_analysis.py
RUN python3 /opt/Mini_Capstone_project/request.py
RUN python3 /opt/Mini_Capstone_project/server.py
EXPOSE 5000