FROM centos
LABEL name=ashutoshh
RUN dnf install httpd -y
COPY index.html /var/www/html/
EXPOSE 80 
# default port of app/ server - when container got created
# use 80 port only
ENTRYPOINT  httpd -DFOREGROUND 
# httpd -DFOREGROUND  == systemctl start httpd 