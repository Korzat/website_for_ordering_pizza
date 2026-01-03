FROM ubuntu:latest
LABEL authors="mikhail"

ENTRYPOINT ["top", "-b"]