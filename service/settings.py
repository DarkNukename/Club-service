"""
Django settings for service project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j5e++182xivs@vxkpv@*7hitn3eu=al=b!bnq-=51*@ghd0k_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['secure-brook-79251.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clubs',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'

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

WSGI_APPLICATION = 'service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_SERVICE_BASE_URL = 'http://127.0.0.1:8000/' if DEBUG else 'https://polar-shelf-60214.herokuapp.com/'
STATISTIC_SERVICE_BASE_URL = 'http://127.0.0.1:8004/'
DANCERS_SERVICE_BASE_URL = 'http://127.0.0.1:8001/' if DEBUG else 'https://fierce-plains-12493.herokuapp.com/'
COMPETITIONS_SERVICE_BASE_URL = 'http://127.0.0.1:8003/' if DEBUG else 'https://desolate-badlands-42848.herokuapp.com/'

SERVICE_ID = 'Clubs'
SERVICE_SECRET = 'qwerty'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'basic': {
            'format': '\n%(asctime)s - %(levelname)s - %(module)s - %(message)s'
        }
    },
    'handlers': {
        'basic': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'basic'
        }
    },
    'loggers': {
        'members_log': {
            'level': 'INFO',
            'handlers': ['basic']
        },
        'clubs_log': {
            'level': 'INFO',
            'handlers': ['basic']
        },
        'error_log': {
            'level': 'INFO',
            'handlers': ['basic']
        }
    }
}

CORS_ORIGIN_ALLOW_ALL = True

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
