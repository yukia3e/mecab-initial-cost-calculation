# IMAGE: yukia3/mecab-initial-cost-calculation

FROM ubuntu:latest

WORKDIR /root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    locales \
    supervisor \
    git \
    make \
    curl \
    file \
    swig \
    vim \
    xz-utils \
    mecab \
    libmecab-dev \
    mecab-ipadic \
    mecab-ipadic-utf8 \
    patch \
    openssl \
    sudo \
    python3 \
    python3-pip \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i -e "s/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/" /etc/locale.gen

RUN locale-gen ja_JP.utf8
ENV LANG="ja_JP.utf8" \
    LANGUAGE="ja_JP.utf8" \
    LC_ALL="ja_JP.utf8"

# install Mecab
RUN export GIT_SSL_NO_VERIFY=1 && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN export GIT_SSL_NO_VERIFY=1 && ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a -y

RUN pip3 install --upgrade pip \
    && pip install --upgrade mecab-python3

RUN cp /etc/mecabrc /usr/local/etc/