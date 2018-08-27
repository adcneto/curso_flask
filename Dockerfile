FROM registry.intranet.pagseguro.uol/base/debian:latest
MAINTAINER l-pd-darwin
LABEL source="https://stash.uol.intranet/scm/ygg/garm-stress.git" \
    maintainer="l-pd-darwin" \
    author="l-pd-darwin" \
    slack="#darwin"
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
# ARG http_proxy=http://pagseguro.proxy.srv.intranet:80
# ARG https_proxy=http://pagseguro.proxy.srv.intranet:80
# download stress-ng sources

RUN apt-get update && \
    apt-get -y install python3.5 python3-pip stress-ng && \
    pip3 install --no-cache-dir -r requirements.txt &&\
    apt-get clean
# ENV http_proxy =
# ENV https_proxy =


EXPOSE 8080
EXPOSE 5000
EXPOSE 80
# EXPOSE 443

CMD ["python3.5", "ExemploFlask.py"]