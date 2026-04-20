# reutiman.one
This is the source code for my personal website. Go check it out at [reutiman.one](https://reutiman.one)

## Installation

```
$ git clone https://github.com/vxnxnt/reutiman.one.git
$ cd reutiman.one
```

Add a private key to use with Anubis:

```
$ openssl rand -hex 32 > anubis_key.priv
```

## Usage

Build the Dockerfile and start uWSGI with Anubis:

```
$ docker compose pull
$ docker compose up -d
$ docker compose up -d uwsgi    # Start only uWSGI without anubis
```

Rebuild when making changes:

```
$ docker compose down && docker compose up -d --build
```