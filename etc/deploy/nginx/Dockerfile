# pull official base image
FROM nginx:1.17-alpine
LABEL author="Gabriel Conrado <gabaconrado@gmail.com>"

RUN mkdir /etc/server
COPY entrypoint.sh /etc/server
RUN chmod +x /etc/server/entrypoint.sh

RUN rm /etc/nginx/conf.d/default.conf
COPY peculiar-fox.conf /etc/server

COPY servercert.pem /etc/server
COPY serverkey.pem /etc/server

ENTRYPOINT [ "/etc/server/entrypoint.sh" ]
