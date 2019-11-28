#!/bin/sh

# Install dependencies and update the database
if [ $DEBUG -eq 1 ]; then
    REQFOLDER="development"
else
    REQFOLDER="deploy"
fi
pip install -r etc/base/requirements.txt
pip install -r etc/$REQFOLDER/requirements.txt
python manage.py migrate --no-input

exec "$@"
