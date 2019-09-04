import os
import logging
import environ

ROOT_DIR = environ.Path(__file__) - 2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool, False), )  # set default values and casting
env_file = str(ROOT_DIR.path('.env'))
env.read_env(env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# Application definition

LOCAL_APPS = [
    'users',
    'wallet',
    'django_countries',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    'django_filters',
    'crispy_forms',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'users.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# to enable the site's framework
SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True

WSGI_APPLICATION = 'e_wallet.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend', 'webpack-stats.json'),
    }
}

# Logging
def levelname_filter(*args):
    class LevelNameFilter(logging.Filter):
        def filter(self, record):
            return record.levelname.lower() in args
    return LevelNameFilter


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'debug_only': {
            '()': levelname_filter('debug'),
        },
        'info_only': {
            '()': levelname_filter('info'),
        },
        'warn_only': {
            '()': levelname_filter('warning'),
        },
        'error_only': {
            '()': levelname_filter('error', 'critical'),
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'sitelog.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'debug.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'info': {
            'level': 'INFO',
            'filters': ['info_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'info.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['warn_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'warning.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'error.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['warning', 'error', 'default'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'default': {
            'handlers': ['console', 'default', 'debug', 'info'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
