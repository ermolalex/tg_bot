#!/bin/bash

# Start the first process
gunicorn --bind 0.0.0.0:8000 config.wsgi &

sleep 2

# Start the second process
python manage.py start_zulip_listener &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?