#!/bin/bash

ps -ef | grep 'flask_webServer.py' | awk '{print $2}' | xargs kill

nohup python3.6 flask_webServer.py 80 >nohup.out &
