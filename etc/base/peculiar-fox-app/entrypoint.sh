#!/bin/sh

pip install -r /etc/base/requirements.txt

# Install dependencies and update the database
if [ ${DEBUG} -eq 1 ]; then
    REQUIREMENTS_SUFIX="development"
else
    REQUIREMENTS_SUFIX="deploy"
    python manage.py collectstatic --no-input
fi

pip install -r /etc/requirements-${REQUIREMENTS_SUFIX}.txt
python manage.py migrate --no-input

exec "$@"
