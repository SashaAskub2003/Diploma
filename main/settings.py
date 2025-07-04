"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import string
import sys

import dj_database_url
from django.conf.global_settings import AUTH_USER_MODEL
from decouple import config
from django.templatetags.static import static
import logging

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# недействительный ключ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние приложения
    # "debug_toolbar",
    'imagekit',

    # Созданные приложения
    "app",
    "tests",
    "users",
    'csp'
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    "csp.middleware.CSPMiddleware",
    'tests.middlewares.TestExitMiddleware',
    "app.middleware.coop_policy_middleware",
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        "default": dj_database_url.config(
            default="postgres://test:root@localhost:5432/Tests", conn_max_age=600
        )
    }

    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'Tests',
    #     'USER': 'test',
    #     'PASSWORD': 'root',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # 
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / 'cache',
    }
}


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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kyiv'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'


# # Дополнительные настройки для WhiteNoise
# if 'test' in sys.argv:
#     # Используем стандартное хранилище для тестов, чтобы избежать ошибок с манифестом
#     STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# else:
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     BASE_DIR / "app/static",
#     BASE_DIR / "tests/static",
#     BASE_DIR / "static", 'users'
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static' , 'media')

AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/user/login/'

LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'users.backends.EmailBackend',
    # 'django.contrib.auth.backends.ModelBackend'
)

#  # Для тестирования

# Включаем поддержку отправки писем в Django
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='smpt.gmail.com')  # Пример для Gmail
EMAIL_PORT = config('EMAIL_PORT', cast=int) # Используем порт для TLS

# Данные для авторизации
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Безопасное соединение
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)  # Используется чаще всего
# EMAIL_USE_SSL = True # Для некоторых серверов можно вместо TLS

# Указываем «с обратным адресом» для всех писем
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'DEFAULT_SECRET_KEY')

# Если запускается на локальном сервере просто закоментировать
ALLOWED_HOSTS  = ['localhost', '127.0.0.1', 'yourdomain.com']

# SSL (для безопасности данных)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


CSP_DEFAULT_SRC = ("'self'", "https://teststepbucket.s3.amazonaws.com")
CSP_SCRIPT_SRC = ("'self'", "https://teststep-54d2adad5311.herokuapp.com", "127.0.0.1", "https://teststepbucket.s3.amazonaws.com")
CSP_STYLE_SRC = ("'self'", "https://teststep-54d2adad5311.herokuapp.com", "127.0.0.1", "https://teststepbucket.s3.amazonaws.com")
CSP_IMG_SRC = ("'self'", "data:", "https://teststep-54d2adad5311.herokuapp.com", "127.0.0.1", "https://teststepbucket.s3.amazonaws.com")
CSP_FONT_SRC = ("'self'", "https://teststep-54d2adad5311.herokuapp.com", "127.0.0.1", "https://teststepbucket.s3.amazonaws.com")
CSP_CONNECT_SRC = ("'self'", "https://teststepbucket.s3.amazonaws.com")
CSP_OBJECT_SRC = ("'none'")
CSP_FRAME_SRC = ("'none'",)
CSP_REPORT_ONLY = True  # Включаем режим отчёта
CSP_REPORT_URI = "/csp-report/"  # Эндпоинт для отчётов


if DEBUG:
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER = None

# SECURE_REFERRER_POLICY = 'no-referrer'

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

# НАСТРОЕЧКИ для AMAZON S3

# Настройки для использования S3
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')

# Указываем, что файлы должны быть публичными
AWS_DEFAULT_ACL = 'public-read'

# Настройки для хранения медиа файлов на S3 и для тестов исполбьзуем локальное хранилище
if "test" in sys.argv:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Настройки для статических файлов (если нужно)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Политика для загрузки файлов
AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

AWS_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    'ContentDisposition': 'inline',
}


UNFOLD = {
    "SITE_HEADER": "Teststep",
    "TEXT": {
        "HEADER": "text-primary-500", # Молочный цвет для заголовков
        "PARAGRAPH": "text-gray-200",  # Светло-серый для основного текста
        "SECONDARY": "text-gray-400",  # Серый для второстепенного текста
    },
    "ELEMENTS": {
        "CARD": "bg-dark-400 border-dark-300", # Чуть светлее фон для карточек
        "TABLE": {
            "HEADER": "bg-dark-300",           # Фон заголовка таблицы
            "ROW": "hover:bg-dark-200",        # Подсветка строк при наведении
        }
    },
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "114 96 245",
            "600": "35 35 35",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "114 96 245",
            "950": "59 7 100",
        }, 
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
    },

    "STYLES": [
        lambda request: static("css/unfold.css"),
    ],

    "SITE_TITLE": 'Teststep',  # Название панели

    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("icons/favicon.svg"),
        },
    ],

    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _(""),
                
                "separator": False,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Головна панель"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                    }
                ]
            },
            {
                "title": _("Користувачі і группи"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Користувачі"),
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("Групи"),
                        "link": reverse_lazy("admin:users_usersgroup_changelist"),
                    },
                    {
                        "title": _("Членство користувача в групах"),
                        "link": reverse_lazy("admin:users_usersgroupmembership_changelist"),
                    },
                    {
                        "title": _("Спроби входу"),
                        "link": reverse_lazy("admin:users_loginattempt_changelist"),
                    },
                    {
                        "title": _("Email повідомлення по тестам"),
                        "link": reverse_lazy("admin:users_emailtestnotyficateuser_changelist"),
                    },
                    {
                        "title": _("Додати студентів"),
                        "link": reverse_lazy("admin:adding_students")
                    }
                ]
            },
            {
                "title": _("Тести"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items":[ 
                    {
                        "title": _("Категорії тестів"),
                        "link": reverse_lazy("admin:tests_categories_changelist")
                    },
                    {
                        "title": _("Тести"),
                        "link": reverse_lazy("admin:tests_tests_changelist")
                    },
                    {
                        "title": _("Групи для питань"),
                        "link": reverse_lazy("admin:tests_questiongroup_changelist")
                    },
                    {
                        "title": _("Питання"),
                        "link": reverse_lazy("admin:tests_question_changelist")
                    },
                    {
                        "title": _("Відповіді"),
                        "link": reverse_lazy("admin:tests_answer_changelist")
                    },
                    {
                        "title": _("Відповіді встановлення відповідності"),
                        "link": reverse_lazy("admin:tests_matchingpair_changelist")
                    },
                ]
            },
            {
                "title": _("Перевірка тестів і Результати"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Результати тестів"),
                        "link": reverse_lazy("admin:tests_testresult_changelist")
                    },
                    {
                        "title": _("Тести на перевірку"),
                        "link": reverse_lazy("admin:tests_testsreviews_changelist")
                    },
                ]
            }
        ]
    },

    
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters" : {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {message}",
#             "style": "{"
#         },
#         'simple': {
#             "format": "{levelname} {message}",
#             "style": "{"
#         },
#         "detailed": {
#             "format": "{levelname}|{asctime}|{pathname}:{lineno}| {message} {exc_info}",
#             "style": "{",
#         }
#     },
#     "handlers": {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },

#         # "sql_file": {
#         #     "level": "DEBUG",
#         #     "class": "logging.FileHandler",
#         #     "filename": BASE_DIR / "logs"/ "sql.log",
#         #     "formatter": "verbose"
#         # },

#         # "debug_log": {
#         #     "level": "DEBUG",
#         #     "class": "logging.FileHandler",
#         #     "filename": BASE_DIR / "logs"/ "debug.log",
#         #     "formatter": "verbose"
#         # },

#         # "error_file": {
#         #     "level": "ERROR",
#         #     "class": "logging.FileHandler",
#         #     "filename": BASE_DIR / "logs"/ "errors.log",
#         #     "formatter": "detailed",
#         # },
#         # "warning_file": {
#         #     "level": "WARNING",
#         #     "class": "logging.FileHandler",
#         #     "filename": BASE_DIR / "logs"/ "warnings.log",
#         #     "formatter": "detailed"
#         # },
#         # "critical_errors": {
#         #     "level": "CRITICAL",
#         #     "class": "logging.handlers.RotatingFileHandler",
#         #     "filename": BASE_DIR / "logs" / "critical.log",
#         #     "formatter": "detailed",
#         #     "maxBytes": 5 * 1024 * 1024,  # 5MB
#         #     "backupCount": 3,  # Хранить 3 старых файла
#         # },

#         # "console_log": {
#         #     "level": "INFO",
#         #     "class": "logging.StreamHandler",
#         #     "formatter": "verbose"
#         # },

#         "logtail": {
#             "class": "logtail.LogtailHandler",
#             "source_token": config("BETTERSTACK_SOURCE_TOKEN"),
#             "host": config("INGESTING_HOST"),
#         }

#     },
#     "loggers": {
#         "django.db.backends": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#             "propagate": True,
#         },

#         "django": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#         "django.request": {
#             "handlers": [ "logtail", "console",],
#             "level": "ERROR",

#         }
#     },
# }


SENTRY_DSN = config('SENTRY_DSN', default=None)

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        send_default_pii=True,
        integrations=[
            DjangoIntegration(
                transaction_style='function_name'
            )
        ],
        traces_sample_rate=1.0,

    )