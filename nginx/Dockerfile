FROM nginx:alpine

ARG NGINX_CONFIG_FILE

RUN rm -f /etc/nginx/conf.d/default.conf

RUN echo Building nginx with environment="${NGINX_CONFIG_FILE}"

COPY ${NGINX_CONFIG_FILE} /etc/nginx/conf.d