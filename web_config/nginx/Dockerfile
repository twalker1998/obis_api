FROM alpine:3.12
LABEL maintainer="Tyler Walker <twalker1998@gmail.com>"

# Install packages and remove default server definition
RUN apk --no-cache add php7 php7-fpm php7-opcache php7-mysqli php7-json php7-openssl php7-curl \
    php7-zlib php7-xml php7-phar php7-intl php7-dom php7-xmlreader php7-ctype php7-session \
    php7-mbstring php7-gd nginx supervisor curl vim wget && \
    rm /etc/nginx/conf.d/default.conf

# Configure nginx
COPY /opt/obis/api_code/web_config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY /opt/obis/api_code/web_config/nginx/default.conf /etc/nginx/conf.d/default.conf

# Configure PHP-FPM
COPY /opt/obis/api_code/web_config/php/fpm-pool.conf /etc/php7/php-fpm.d/www.conf
COPY /opt/obis/api_code/web_config/php/php.ini /etc/php7/conf.d/custom.ini

# Configure supervisord
COPY /opt/obis/api_code/web_config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup document root
RUN mkdir -p /var/www/html

# Make sure files/folders needed by the processes are accessible when they run under the nobody user
RUN chown -R nobody.nobody /var/www/html && \
    chown -R nobody.nobody /run && \
    chown -R nobody.nobody /var/lib/nginx && \
    chown -R nobody.nobody /var/log/nginx

# Switch to use a non-root user from here on
USER nobody

# Add applications
WORKDIR /var/www/html
COPY --chown=nobody /opt/obis/obis/ /var/www/html/
COPY --chown=nobody /opt/obis/obis_db_scripts/ /var/www/html/

# Expose the port nginx is reachable on
EXPOSE 8081

# Let supervisord start nginx & php-fpm
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

# Configure a healthcheck to validate that everything is up and running
HEALTHCHECK --timeout=10s CMD curl --silent --fail http://127.0.0.1:8080/fpm-ping
