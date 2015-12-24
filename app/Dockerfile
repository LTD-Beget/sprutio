FROM beget/sprutio-python
MAINTAINER "Maksim Losev <mlosev@beget.ru>"

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY init-ssl.sh /etc/cont-init.d/10-init-ssl.sh

COPY run-app.sh /etc/services.d/app/run
COPY ./ /app/

WORKDIR /app/
