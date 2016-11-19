#!/usr/bin/env bash

killall gunicorn
/home/coon/.local/bin/gunicorn --bind=0.0.0.0:8000 wsgi_cutie:application
