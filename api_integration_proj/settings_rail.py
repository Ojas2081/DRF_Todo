from api_integration_proj.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['todo-app-ojas.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://todo-app-ojas.up.railway.app/']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": config('DATABASE_USER'),
        "PASSWORD": config('DATABASE_PASSWORD'),
        "HOST": config('DATABASE_HOST'),
        "PORT": config('DATABASE_PORT'),
        "NAME": config('DATABASE_NAME'),
        "OPTIONS": {
            "sslmode": "require"
        },
    }
}
