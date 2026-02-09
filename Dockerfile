FROM ubuntu:latest
LABEL authors="maksu"

ENTRYPOINT ["top", "-b"]