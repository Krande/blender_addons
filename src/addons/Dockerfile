FROM ubuntu:latest

RUN apt-get update && apt-get install build-essential -y
RUN apt-get install wget -y
COPY . .

RUN make dist PLATFORM=win PYVERSION=py39