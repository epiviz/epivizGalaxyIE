FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential libssl-dev gcc curl git supervisor

RUN apt-get install -y python3 python-virtualenv python3-dev apache2 zlib1g-dev liblzma-dev libbz2-dev

# Setup UI
COPY client /var/www/html
# RUN apachectl -D FOREGROUND &

# setup API
RUN mkdir /var/www/api
RUN chmod -R 777 /var/www/api/

COPY ./srv/* /var/www/api/
WORKDIR /var/www/api

ENV VIRTUAL_ENV=/var/www/api/env
RUN virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Deps
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 80 8000

# Setup Supervisor
RUN mkdir -p /var/log/supervisor
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# RUN /usr/bin/supervisord
CMD ["/usr/bin/supervisord"]

# Run App
# COPY ./srv/epiviz.py /var/www/api/env
# CMD ["python", "/var/www/api/epiviz.py"]
# RUN python /var/www/api/epiviz.py &
# CMD ["apachectl", "-D", "FOREGROUND"]
