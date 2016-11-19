#!/usr/bin/env bash

gunicorn --config=/home/coon/CoonAsk/config/gunicorn.conf wsgi_cutie:application
