FROM python:3.4
MAINTAINER "Maksim Losev <mlosev@beget.ru>"

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

ENTRYPOINT ["/init"]

RUN apt-get update -qq && \
    apt-get install --no-install-recommends -qq -y \
        libacl1-dev \
        libarchive-dev

ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2
