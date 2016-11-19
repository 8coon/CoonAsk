#!/bin/sh

# =====[ User vars start ]=====
PROJECT_NAME=CoonAsk
# =====[ User vars end ]=====

rm /etc/nginx/sites-enabled/default
ln -s ~/$PROJECT_NAME/config/nginx.conf /etc/nginx/sites-enabled/default

killall gunicorn
gunicorn --daemon --config=/home/coon/CoonAsk/config/gunicorn.conf CoonAsk.wsgi:application
service nginx restart
