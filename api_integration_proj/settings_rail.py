from api_integration_proj.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-f0e9.up.railway.app']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
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
