from .base import *


DEBUG = False

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ADMINS = (
    ('Antonio M Yani', 'yannidimitrova@gmail.com'),
)

ALLOWED_HOSTS = ['.elearningproject.com', ]


# DATABASES = {
#     'default': {
       
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elearning',
        'USER': 'postgres',
        'PASSWORD': 'postgreto',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# text for the console to run the project in production:
# uwsgi --module=elearning.wsgi:application --env=DJANGO_SETTINGS_MODULE=elearning.settings.pro --master --pidfile=/tmp/project-master.pid --http=127.0.0.1:8000 --uid=1000 --virtualenv=/mnt/d/pytek/env/elearning