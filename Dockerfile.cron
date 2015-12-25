FROM beget/sprutio-python
MAINTAINER "Maksim Losev <mlosev@beget.ru>"

RUN apt-get install --no-install-recommends -qq -y cron

COPY run-cron.sh /etc/services.d/cron/run
COPY cron.d/ /etc/cron.d/

VOLUME /tmp/fm
