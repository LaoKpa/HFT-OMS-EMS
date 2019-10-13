FROM ubuntu:18.04

RUN apt-get update \
	&& apt-get install -y build-essential cmake \
	&& apt-get install -y python3 python3-pip \
	&& update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 \
	&& update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

ARG BUILD_TS=null
ENV BUILD_TS ${BUILD_TS}
RUN rm -rf ~/hftapp
COPY . ~/hftapp
WORKDIR ~/hftapp
RUN make clean-cpp clean-py

RUN make build-cpp build-py

RUN make compile

RUN echo "successfully built ${BUILD_TS}."