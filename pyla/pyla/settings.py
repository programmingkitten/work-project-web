"""
Django settings for pyla project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l_z)zitcu_etz4dx_f1z37a)bvr&kps!v#^87-4x2mxf)f7ru1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',
                 'pyla-website.herokuapp.com',
                 ]
DATABASE_URL = 'postgres://jizhxgrgcramzw:eebf00700331b573182cf01db69d9e82f6aec2b7a98b9eb8eeb1cd90f05fac46@ec2-54-228' \
               '-125-183.eu-west-1.compute.amazonaws.com:5432/d3g8nvi95n6bef '
# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'pyla.web',
    'pyla.web_testing',
    'pyla.manage_profiles',
    'pyla.forums',
    'pyla.subscriptions',
    'pyla.user_activity',
    'pyla.administrate',
    'pyla.betscrapper',
    'django_filters',
    "bootstrap5",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pyla.middlewares.handle_exception'
]

ROOT_URLCONF = 'pyla.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyla.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'pyla_soft_db',
#         'USER': 'postgres',
#         'PASSWORD': '1123QwER',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3g8nvi95n6bef',
        'USER': 'jizhxgrgcramzw',
        'PASSWORD': 'eebf00700331b573182cf01db69d9e82f6aec2b7a98b9eb8eeb1cd90f05fac46',
        'HOST': 'ec2-54-228-125-183.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

import dj_database_url

DATABASES['default'] = dj_database_url.config()
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # off only for developing. Must turn on for production
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]
#
# CACHES = {
#
#     'default': {
#
#         'BACKEND':
#
#             'django.core.cache.backends.redis.RedisCache',
#
#         'LOCATION':
#
#             'redis://127.0.0.1:6379',
#
#     }
#
# }

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_ROOT = BASE_DIR / 'static'
# STATIC_URL = 'static/'
#
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = 'static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Extra places for collectstatic to find static files.

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'manage_profiles.AppUser'

LOGIN_URL = reverse_lazy('login user')
LOGIN_REDIRECT_URL = reverse_lazy('index')

import environ

env = environ.Env()
environ.Env.read_env()
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'pylafeedback@gmail.com'
# EMAIL_HOST_PASSWORD = 'pbzlkihxxwnzpjkr'
EMAIL_HOST_USER = 'pylafeedbackcorp@gmail.com'
EMAIL_HOST_PASSWORD = 'oshxquzwhaaterna'
RECIPIENT_ADDRESS = 'vankata294n4@gmail.com'
