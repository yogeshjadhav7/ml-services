#!/usr/bin/env bash

# move to project directory
cd /home/yogesh/ml-apps/ml-services

# start virtualenv
tensorflow

# start the gunicorn process in nohup (background)
nohup gunicorn ml_services.wsgi:application --bind 127.0.0.1:8000 &

