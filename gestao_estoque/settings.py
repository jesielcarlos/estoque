from pathlib import Path
import decouple
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = decouple.config(
    "SECRET_KEY",
    default=""
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.core',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestao_estoque.urls'

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

WSGI_APPLICATION = 'gestao_estoque.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    "default": decouple.config(
        "DATABASE_URL",
        default=decouple.config("DATABASE_URL", default=""),
        cast=dj_database_url.parse
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "https://market.zaoridata.com.br",
    "https://aglut.zaoridata.com.br",
    "https://teste.aglut.zaoridata.com.br",
    "https://api.market.zaoridata.com.br",
    "https://api.aglut.zaoridata.com.br",
]

CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CORS_ALLOW_ALL_ORIGINS = DEBUG
CSRF_TRUSTED_ORIGINS = [
    "https://market.zaoridata.com.br",
    "https://aglut.zaoridata.com.br",
    "https://teste.aglut.zaoridata.com.br",
    "https://api.aglut.zaoridata.com.br",
]


if DEBUG:
    SECURE_CROSS_ORIGIN_OPENER_POLICY = None
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]
    CORS_ALLOWED_ORIGINS += [
        "http://192.168.190.56:3000",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "http://192.168.1.190:8000",
        "http://192.168.1.190",
        "http://atyson.net",
        "http://leo.net",
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://localhost:3001",
        "http://192.168.1.151:3000",
        "http://192.168.1.58:3000",
        "http://10.10.70.76:31423",
        "http://10.10.70.76:31451",
        "http://10.10.70.76:3000",
        "http://10.10.70.76:30285",
        "http://10.10.70.76",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://192.168.24.17:3000",
        "http://192.168.24.17:8000",
        "http://192.168.24.17",
        "http://192.168.24.86",
        "http://192.168.24.86:3000",
        "http://192.168.13.32:3000",
        "http://192.168.13.55:3000",
        "http://192.168.13.32:8000",
        "http://192.168.13.28:3000",
        "http://192.168.13.27:3000",
        "http://192.168.13.28:3001",
        "http://192.168.24.86:8000",
        "http://teste.aglut.zaori.local",
        "http://aglut.zaori.local",
        "http://api.aglut.zaori.local",
        "http://mesotech.aglut.zaori.local",
        "http://localhost.aglut.zaori.local",
        "http://market.zaori.local",
    ]

from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = (
    *default_headers,
    "Zaori-team",
)
