#!/bin/sh

# Install dependencies and update the database
if [ $DEBUG -eq 1 ]; then
    REQUIREMENTS_SUFIX="development"
else
    REQUIREMENTS_SUFIX="deploy"
fi
pip install -r /etc/requirements-base.txt
pip install -r /etc/requirements-${REQUIREMENTS_SUFIX}.txt
python manage.py migrate --no-input

exec "$@"
