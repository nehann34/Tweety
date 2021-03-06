"""
Django settings for tweety project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@lo%cw03o$)bf@@d1si%ot3rghv@e7mhllf+ho_rp_j$m*1+='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

YELLOWANT_CLIENT_ID="WWqQDXm6rCXSrrTKB5fqo28a0bH7VTdSwWMPNv1t"
YELLOWANT_CLIENT_SECRET="YtQKne67Islf1Jrye9HVcrL5aBHGswpQVYdPCWpH6Vy5W0BvnS6zravpdbIEmTSPoVnudNMeWQlYFkxEsPvp6vHhusjfhTFix1FLhcOyykzm8RGmIeOnOyVDAhlGO9KD"
YELLOWANT_VERIFICATION_TOKEN="q6zFD0yakEbVdPaXJpjipYjynqGDipYnOeJPCRE9wPFSuGy5TbNL1676aLzm5dZkeAxoPR2AbtKXwin5xEIn4d3fRrM7Lbw5QCLLtLhOqxVNyP7AScVbt5cmnvcUgBTL"
YELLOWANT_REDIRECT_URL="http://69ab4658.ngrok.io/redirecturl/"

TWITTER_CONSUMER_KEY="LkFkdnjA2GoXrUShct4Ufvhsa"
TWITTER_CONSUMER_SECRET="tSlzkwAe8co1P75Npvybg0KkCcio9plnLnoKCa1s8clfjZdt2Z"

# Application definition

INSTALLED_APPS = [
    'authenticate',
    'authenticate_twitter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tweety.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'tweety.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
