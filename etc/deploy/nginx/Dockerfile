# pull official base image
FROM nginx:1.17-alpine
LABEL author="Gabriel Conrado <gabaconrado@gmail.com>"

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

RUN rm /etc/nginx/conf.d/default.conf
COPY peculiar-fox.conf /etc/nginx/conf.d/

COPY servercert.pem /
COPY serverkey.pem /

ENTRYPOINT [ "/entrypoint.sh" ]
