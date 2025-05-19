# Django with Nginx

This is a template for running Django with Nginx.

It utilizes Supervisor and Gunicorn to serve the Django application.

## Building and running

```bash
docker build --rm -f Dockerfile -t practical:latest .
docker run --name practical --rm -p 29125:80 practical:latest
```

## Supervisor

For stacks involving a single Django application, Supervisor is not needed and Gunicorn can be run directly in the entrypoint.

```bash
gunicorn --workers 2 --bind 127.0.0.1:10003 mysite.wsgi:application
```

However, the intention for this app stack was to host multiple Django applications, so Supervisor would be used to manage them all in `gunicorn.conf`.

## TODOs

- move python dependencies to a separate file like `requirements.txt` instead of having it in the Dockerfile
- use a non-root user for Docker container
