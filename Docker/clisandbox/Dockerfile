FROM tjnii_base/debian

# General dev deps
RUN apt-get install -y git
RUN apt-get install -y emacs23-nox
RUN apt-get install -y python
RUN apt-get install -y ipython
RUN apt-get install -y netcat-traditional

RUN apt-get install -y mongodb-clients

# App specific deps
RUN apt-get install -y build-essential 
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN pip install PyMongo
RUN apt-get install -y python-yaml
