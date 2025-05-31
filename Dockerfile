FROM python:3.13-slim-bookworm

# TODO: consider moving Python dependencies outside of Dockerfile
RUN pip install Django gunicorn whitenoise

RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

COPY gunicorn.conf /etc/supervisor/conf.d/
RUN mkdir -p /var/log/gunicorn

RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/mysite
RUN ln -s /etc/nginx/sites-enabled/mysite /etc/nginx/sites-available/mysite

COPY mysite/ /app/mysite

# generate static files for django
RUN python /app/mysite/manage.py collectstatic --noinput

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["/entrypoint.sh"]
