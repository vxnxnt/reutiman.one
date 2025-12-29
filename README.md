# reutiman.one
This is the source code for my personal website. Go check it out at [reutiman.one](https://reutiman.one)

Build and run the Dockerfile with

```
$ docker image build -t uwsgi .
$ podman run \
    -d \
    -p 127.0.0.1:33332:33332 \
    -v /some/path/templates:/var/app/templates:Z \
    -v /some/pathstatic:/var/app/static:Z \
    uwsgi
```
