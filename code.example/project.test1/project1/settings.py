# coding: utf-8

"""
Django settings for project1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2y_a)bnxyjuy-+04v+&o&^5er6ob18g2(#ko!9c&pe%73g2=#p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'app1',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project1.urls'

WSGI_APPLICATION = 'project1.wsgi.application'

#
# ロギングを利用するために追記した
#
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(asctime)s [%(levelname)s] (pid:%(process)d) (thread:%(thread)d) <%(module)s> %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'filters': {
	},
	'handlers': {
		'null': {
			'level':'DEBUG',
			'class':'django.utils.log.NullHandler',
		},
		'logfile': {
			'level': 'DEBUG',
			'class':'logging.handlers.WatchedFileHandler',
			'filename': '/var/log/django/application.log',
			'formatter': 'verbose',
		},
		'console': {
			'level':'DEBUG',
			'class':'logging.StreamHandler',
			'formatter': 'verbose',
		},
	},
	'loggers': {
		'app1': {
			'handlers': ['logfile'],
			'level': 'DEBUG',
		},
	}
}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

APPEND_SLASH = False




#
# cookie に関するパラメータを追記した
#
# SESSION_COOKIE_AGE = -1 #sec
SESSION_COOKIE_NAME = 'sessionid'



#
# in-memory session を利用するために追記した
#
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
CACHES = {
	'default' : {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'LOCATION': 'WE ARE THE WORLD'
	}
}
SESSION_COOKIE_HTTPONLY = True

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#
# 変更した
#
LANGUAGE_CODE = 'ja-JP'

#
# 変更した
#
TIME_ZONE = 'Japan'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
