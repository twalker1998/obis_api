FROM php:7.2-apache
MAINTAINER Tyler Walker <twalker1998@gmail.com>

# Install necessary packages.
RUN apt-get update && apt-get install -y vim libpq-dev && docker-php-ext-install pgsql

EXPOSE 80
