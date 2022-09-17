from .settings import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True),
    ADMIN=(str, ADMIN_PAGE_URL),
    ALLOWED_HOSTS=(list, ALLOWED_HOSTS),
    SECRET_KEY=(str, SECRET_KEY),
    PROD_DB=(bool, PROD_DB),
    ENV=(str, ''),
)
environ.Env.read_env(BASE_DIR / ".env")


DEBUG = env("DEBUG")
ADMIN = env("ADMIN")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
ENV = env('ENV')

if not DEBUG:     
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 2592000 # 1 month in seconds
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


if PROD_DB:
    # postgres
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT")
        }
        
    }
    
    # Mysql
    
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql_psycopg2",
    #         "NAME": env("DB_NAME"),
    #         "USER": env("DB_USER"),
    #         "PASSWORD": env("DB_PASSWORD"),
    #         "HOST": env("DB_HOST"),
    #         "PORT": env("DB_PORT"),
    #     }
        
    # }
