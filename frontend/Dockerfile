FROM mhart/alpine-node:12

# install dependencies
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm ci

# Copy all local files into the image.
COPY . .
