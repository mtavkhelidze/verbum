FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev libblas3 liblapack3 liblapack-dev libblas-dev
COPY requirements.txt /
RUN pip install -r /requirements.txt

#
#
#RUN set -xe \
#  && apt-get update \
#  && apt-get install -y python3
#ADD requirements.txt .
#RUN pip install -r requirements.txt

## setup
#COPY verbum-src.tar .
#
#RUN tar xf verbum-src.tar
#RUN rm -f verbum-src.tar
#
## server
#RUN pip install -r requirements.txt
#
## client
#WORKDIR ./client
#RUN npm install
#RUN npm run build
#
#CMD ["npm", "start"]
