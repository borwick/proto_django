Contained herein is some stuff I've found useful when setting up new Django projects.

You'll need to set up`proto_django/settings/local_settings.py`, but to review/find the variables you need to set you can run `python manage.py test proto_django.tests` until you don't get any errors.

Customizing for your environment
=====

1. Rename the project:

        PROJECT_NAME=example
        find * -type f -print0 | xargs -0 perl -i.bak -pe "s|proto_django|$PROJECT_NAME|g"
        find . -name '*.bak' -exec rm {} \;
        mv proto_django $PROJECT_NAME

2. Set up rabbitmq:

        PROJECT_NAME=example
        RABBIT_USER=$PROJECT_NAME
        RABBIT_VHOST=$PROJECT_NAME
        sudo rabbitmqctl add_user $RABBIT_USER
        sudo rabbitmqctl add_vhost $RABBIT_VHOST
        sudo rabbitmqctl set_permissions -p $RABBIT_VHOST $RABBIT_USER '.*' '.*' '.*'

3. Generate a `SECRET_KEY` for your local settings:

        from django.utils.crypto import get_random_string
        
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        get_random_string(50, chars)

4. Set up your `local_settings.py` in `$PROJECT_NAME/settings/local_settings.py`:

        SECRET_KEY = u'CONTENTS-FROM-THE-ABOVE-STEP'
        DATABASES = { 'default': { ... } }
        BROKER_URL = "amqp://username:pass@server/nodename"
        CELERY_RESULT_BACKEND = "amqp"
        CELERY_CONCURRENCY = 1
        CELERYD_NODES = "w1"

5. Remove proto_django from the git remote list:

        git remote rm origin
