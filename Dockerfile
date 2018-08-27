FROM gliderlabs/alpine:3.3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

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