#DOCKER-VERSION    1.12.5
# 
# Dockerizing fastweb: Dockerfile for building Centos images
FROM index.tenxcloud.com/yang123456789/flask
MAINTAINER yangjiajia

RUN mkdir -p /identification

ADD identification /identification

WORKDIR /identification

EXPOSE 9530

ENTRYPOINT python main.py 0.0.0.0:9530
