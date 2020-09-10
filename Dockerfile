FROM python:3.7-buster
LABEL maintainer="Jeffrey James"

# install nginx
RUN apt-get update && apt-get install nginx vim gunicorn -y --no-install-recommends
RUN apt-get remove -y libapache2-mod-python libapache2-mod-wsgi
RUN apt-get install -y libapache2-mod-wsgi-py3
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/bookapi
COPY requirements.txt entrypoint.sh /opt/app/
RUN chmod 755 /opt/app/entrypoint.sh
#COPY .pip_cache /opt/app/pip_cache/
COPY ./ /opt/app/bookapi/
WORKDIR /opt/app
RUN pip install -r requirements.txt #--cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8000
STOPSIGNAL SIGTERM

ENTRYPOINT ["/opt/app/entrypoint.sh"]