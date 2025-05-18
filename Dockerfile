FROM python:3.13-slim-bookworm

COPY mysite/ /app/mysite

RUN pip install Django gunicorn
COPY gunicorn.conf /etc/supervisor/conf.d/
RUN mkdir -p /var/log/gunicorn

RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/mysite
RUN ln -s /etc/nginx/sites-enabled/mysite /etc/nginx/sites-available/mysite

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]