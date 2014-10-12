Contained herein is some stuff I've found useful when setting up new Django projects.

You'll need to set up`procmap/settings/local_settings.py`, but to review/find the variables you need to set you can run `python manage.py test procmap.tests` until you don't get any errors.

Prerequisites
=====

- Postgres
- Python 2.7
- RabbitMQ
- virtualenv and virtualenv-wrapper

Customizing for your environment
=====

1. Rename the project:

        PROJECT_NAME=example
        find * -type f -print0 | xargs -0 perl -i.bak -pe "s|procmap|$PROJECT_NAME|g"
        find . -name '*.bak' -exec rm {} \;
        mv procmap $PROJECT_NAME

2. Set up rabbitmq:

        PROJECT_NAME=example
        RABBIT_USER=$PROJECT_NAME
        RABBIT_VHOST=$PROJECT_NAME
        RABBIT_PASS=
        sudo rabbitmqctl add_user $RABBIT_USER $RABBIT_PASS
        sudo rabbitmqctl add_vhost $RABBIT_VHOST
        sudo rabbitmqctl set_permissions -p $RABBIT_VHOST $RABBIT_USER '.*' '.*' '.*'

3. Install virtualenv and modules so that you can have Django:

        make pulldown
        workon $PROJECT_NAME

3. Generate a `SECRET_KEY` for your local settings:

        from django.utils.crypto import get_random_string
        
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        get_random_string(50, chars)

4. Set up your `local_settings.py` in `$PROJECT_NAME/settings/local_settings.py`:

        SECRET_KEY = u'CONTENTS-FROM-THE-ABOVE-STEP'
        BROKER_URL = "" # have the shell echo "amqp://$RABBIT_USER:$RABBIT_PASS@localhost/$RABBIT_VHOST"
        CELERY_RESULT_BACKEND = "amqp"
        CELERY_CONCURRENCY = 1
        CELERYD_NODES = "w1"

        # Example:
        DATABASES = {    'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'DATABASE-NAME',
                'USER': 'DATABASE-USER',
                'PASSWORD': 'DATABASE-PASS',
                'HOST': 'DATABASE-HOST',
                'PORT': 'DATABASE-PORT',
            }
        }


5. Remove procmap from the git remote list:

        git remote rm origin
