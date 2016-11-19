#!/usr/bin/env bash

killall gunicorn
gunicorn --bind=0.0.0.0:8000 wsgi_cutie:application
