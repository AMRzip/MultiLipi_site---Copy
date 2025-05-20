from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["https://multilipi.azurewebsites.net","https://multilipi.com","https://www.multilipi.com", "https://multilipi-fedbbqeqhaarc2fu.centralindia-01.azurewebsites.net"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # "storages",
    'tailwind',
    'theme',
    'main',
    "app",
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "main.middlewear.ReferralLinkCookieMiddleware",
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'csp.middleware.CSPMiddleware',
]

# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_STYLE_SRC = ("'self'",)
# CSP_IMG_SRC = ("'self'",)

ROOT_URLCONF = 'MultiLipi_site_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates",],
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

WSGI_APPLICATION = 'MultiLipi_site_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':"multilipi-database",
#         'HOST':"multilipi-server.postgres.database.azure.com",
#         'PORT':"5432",
#         'USER':'Kunal',
#         'PASSWORD':os.getenv('POSTGRESQL_PASSWORD'),
#     }
# }

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':"postgres",
        'HOST':"multilipi-web-server.postgres.database.azure.com",
        'PORT':"5432",
        'USER':'MultiLipiDB',
        'PASSWORD':os.getenv('POSTGRESQL_PASSWORD'),
    }
}

TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIAFILES_DIRS = [BASE_DIR / 'media']

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DEFAULT_FILE_STORAGE = 'MultiLipi_site_django.azure.AzureMediaStorage'
# STATICFILES_STORAGE = 'MultiLipi_site_django.azure.AzureStaticStorage'
# STATIC_LOCATION = "static"
# MEDIA_LOCATION = "media"
# AZURE_ACCOUNT_NAME = "multilipiwebstorage"
# AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
# STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
# MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'

CKEDITOR_BASEPATH = f'{STATIC_URL}ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = f'{MEDIA_URL}uploads/'
CKEDITOR_CONFIGS= {
    'default': {
       'toolbar': 'full',
       'font_defaultLabel': 'Cosmic Sans MS'
    }
}