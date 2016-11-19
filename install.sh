#!/bin/sh

# =====[ User vars start ]=====
PROJECT_NAME=CoonAsk
# =====[ User vars end ]=====

rm /etc/nginx/sites-enabled/default
ln -s ~/$PROJECT_NAME/config/nginx.conf /etc/nginx/sites-enabled/default

# rm /etc/gunicorn.d/wsgi
# ln -s ~/$PROJECT_NAME/config/gunicorn.conf /etc/gunicorn.d/wsgi

service nginx restart
service gunicorn stop
gunicorn --daemon --config=~/$PROJECT_NAME/config/gunicorn.conf
