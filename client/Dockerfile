FROM node:alpine

WORKDIR /usr/app
RUN npm install --global pm2

COPY ./package*.json ./
RUN npm install --production

ADD ./ ./

ARG API_URL
RUN npm run build

EXPOSE ${CLIENT_PORT}
CMD pm2-runtime npm -- start -- -p ${CLIENT_PORT}
