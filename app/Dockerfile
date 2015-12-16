FROM beget/fmcore-python

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY run-app.sh /etc/services.d/app/run

COPY ./ /app/

WORKDIR /app/

VOLUME /app/public
