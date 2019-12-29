#!/usr/bin/env bash

(
  cd src
  export FLASK_APP=app.py
  export FLASK_ENV=development
  flask run --reload
)
