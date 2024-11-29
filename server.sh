#!/usr/bin/env sh

source venv/bin/activate;uwsgi --http-socket localhost:33332 --wsgi-file start.py
