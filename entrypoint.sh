#!/bin/bash
cd /code/
/opt/.venv/bin/python manage.py migrate
/opt/.venv/bin/python manage.py collectstatic --noinput
echo "iniitialized"
/opt/.venv/bin/python manage.py runserver 0.0.0.0:8000
