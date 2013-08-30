#!/usr/bin/env bash
cd $(dirname "${BASH_SOURCE[0]}")
cd ..

VENV='proto_django'

if [ -e ../.venv ]
then
  VENV=$(cat ../.venv)
fi

. ~/.virtualenvs/$VENV/bin/activate
. ~/.virtualenvs/$VENV/bin/postactivate

python manage.py clearsessions
