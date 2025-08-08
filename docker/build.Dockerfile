FROM ubuntu:latest
LABEL authors="marek"

RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get -y install tzdata

RUN apt-get update \
  && apt-get install -y build-essential \
      make \
    cmake \
    gdb \
    yacc \
    python3 \
  && apt-get clean