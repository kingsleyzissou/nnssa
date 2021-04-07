FROM lambci/lambda:build-python3.7

ENV PYTHON_VERSION=3.7.7
ENV FFMPEG_VERSION=4.3.2

RUN yum install -y tar xz yum-utils

WORKDIR /tmp

RUN curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz
RUN tar xf Python-${PYTHON_VERSION}.tar.xz

RUN mkdir -p /tmp/ffmpeg
WORKDIR /tmp/ffmpeg

RUN curl -o ffmpeg-${FFMPEG_VERSION}-amd64-static.tar.xz https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
RUN tar xf ffmpeg-${FFMPEG_VERSION}-amd64-static.tar.xz

WORKDIR /tmp/ffmpeg/ffmpeg-${FFMPEG_VERSION}-amd64-static

RUN mkdir -p /opt/bin

RUN mv ffmpeg /opt/bin/
RUN mv ffprobe /opt/bin/

# set workdir back
WORKDIR /var/task
