#!/bin/bash

echo Starting Gunicorn. ls
python manage.py migrate

python manage.py test


# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn ArticlesApi.wsgi:application \
    --name ArticleContainer \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    "$@"