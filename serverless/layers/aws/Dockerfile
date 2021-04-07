FROM lambci/lambda:build-nodejs12.x

RUN mkdir -p /opt/nodejs

WORKDIR /opt/nodejs

COPY package.json package.json

RUN npm install

# set workdir back
WORKDIR /var/task