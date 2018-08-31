FROM debian:stretch-slim

ENV LANG C.UTF-8

RUN apt-get update -qq && apt-get install -qq -y --no-install-recommends \
# curl and gnupg required to install keys for yarn package
    curl \
    gnupg \
    python3-pip \
    python3-setuptools \
    python3-wheel \
# required to install uWSGI
    build-essential \
    python3-dev
    # ca-certificates \

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq && apt-get install -qq -y --no-install-recommends \
    nodejs \
    yarn
    # yarn \
    # libgconf-2-4

WORKDIR /srv

COPY requirements.txt /srv
RUN pip3 install -r requirements.txt

COPY . /srv/

RUN cd /srv  && yarn install && yarn build
RUN chown -R www-data:www-data /srv/dist
# delete node_modules, not necessary after the build
RUN rm -rf /srv/node_modules

WORKDIR /srv
EXPOSE 8000

CMD uwsgi uwsgi.ini
