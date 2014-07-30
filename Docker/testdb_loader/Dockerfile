FROM tjnii_base/debian

# Deps
RUN apt-get install -y build-essential 
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN pip install PyMongo
RUN apt-get install -y python-yaml

# Loader Script
COPY setupTestDB.py /opt/loader/
COPY testData.yaml  /opt/loader/

ENTRYPOINT ["/opt/loader/setupTestDB.py", "--sourcefile=/opt/loader/testData.yaml"]