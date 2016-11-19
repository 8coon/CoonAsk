#!/usr/bin/env bash

service gunicorn stop
gunicorn --bind=0.0.0.0:8000 wsgi_cutie:application
