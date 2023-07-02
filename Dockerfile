FROM apache/hadoop:3

USER root

# The official image uses a CentOS system
# Update the package repository and install sudo
RUN yum update -y
RUN yum install -y sudo
RUN yum install -y python3

# Keep the docker image running, so that you can connect to it
CMD ["sh", "-c", "tail -f /dev/null"]


