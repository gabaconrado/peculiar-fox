#!/bin/sh

# Check if certificates exist
if ! [ -f "${SERVER_CERTIFICATE}" ] || ! [ -f  "${SERVER_PRIVATE_KEY}" ];
then
    echo "Server certificate and/or private key not found"
    exit 1
fi

# Replace the values in the nginx template for the environment vars
envsubst < /etc/nginx/conf.d/peculiar-fox.conf > /etc/nginx/conf.d/peculiar-fox.conf

exec "$@"
