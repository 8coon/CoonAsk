#!/usr/bin/env bash

service gunicorn stop
gunicorn --bind=0.0.0.0:8080 wsgi_cutie:application
