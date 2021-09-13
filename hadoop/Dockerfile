# Hadoop-basement docker file
FROM ubuntu:latest

ENV TEST 1
ENV DEBIAN_FRONTEND noninteractive

WORKDIR ~

RUN apt-get update && \
	apt-get install openjdk-11-jdk curl wget -y && \
	wget http://apache.mirror.cdnetworks.com/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz && \
	tar -zxvf hadoop-3.3.0.tar.gz

RUN apt-get install openssh-client -y && \
	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
	chmod 600 ~/.ssh/authorized_keys


RUN echo $(dirname $(dirname $(readlink -f $(which java)))) >> .bashrc


CMD echo $TEST
CMD echo $JAVA_HOME
