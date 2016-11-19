#!/usr/bin/env bash

service gunicorn stop
gunicorn --config=/home/coon/CoonAsk/config/gunicorn.conf wsgi_cutie:application
