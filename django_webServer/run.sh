#!/bin/bash

ps -ef | grep 'python3.6 manage.py runserver' | awk '{print $2}' | xargs kill

nohup python3.6 manage.py runserver 0.0.0.0:8080 >nohup.out &
