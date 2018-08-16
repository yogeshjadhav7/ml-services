#!/usr/bin/env bash

# move to project directory
cd /home/yogesh/ml-apps/ml-services

# kill the previously running instance of the service on port 8000
lsof -n -i :8000 | grep LISTEN | awk '{ print $2 }' | uniq | xargs kill -9

# delete the nohup.out file
rm nohup.out

# start the gunicorn process in background using nohup
nohup gunicorn ml_services.wsgi:application --bind 127.0.0.1:8000 &

