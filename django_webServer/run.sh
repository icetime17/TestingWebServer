#!/bin/bash

ps -ef | grep 'python manage.py runserver' | awk '{print $2}' | xargs kill

nohup python manage.py runserver 0.0.0.0:8080 >nohup.out &
