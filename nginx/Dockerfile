# Base on offical NGINX Alpine image
FROM nginx:alpine

# Remove any existing config files
RUN rm /etc/nginx/conf.d/*

# Copy config files
# *.conf files in conf.d/ dir get included in main config
COPY ./default.conf ./

ARG client_port
ARG server_port
RUN envsubst '${client_port} ${server_port}' < ./default.conf > /etc/nginx/conf.d/default.conf
RUN cat /etc/nginx/conf.d/default.conf

# Expose the listening port
EXPOSE 80

# Launch NGINX
CMD [ "nginx", "-g", "daemon off;" ]

