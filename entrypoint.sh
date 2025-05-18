#!/bin/bash

# start nginx
nginx

# start supervisor
/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
