#!/bin/sh

# Replace the values in the nginx template for the environment vars
envsubst < /etc/nginx/conf.d/peculiar-fox.conf > /etc/nginx/conf.d/peculiar-fox.conf

exec "$@"
