FROM node:13.5

# client
WORKDIR /usr/src
COPY client/ .

WORKDIR /usr/src/client
RUN npm install
RUN npm run build

CMD ["npm", "start"]
