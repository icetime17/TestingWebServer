#!/bin/bash

ps -ef | grep 'flask_webServer.py' | awk '{print $2}' | xargs kill

nohup python flask_webServer.py 80 >nohup.out &
