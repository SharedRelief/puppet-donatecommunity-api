FROM tjnii_base/debian

RUN apt-get install -y mongodb-server

COPY mongodb.conf /etc/mongodb.conf

EXPOSE 27017 28017
USER mongodb
# Options listed from the init script
CMD ["/usr/bin/mongod", "--unixSocketPrefix=/var/run/mongodb", "--config=/etc/mongodb.conf", "run"]
