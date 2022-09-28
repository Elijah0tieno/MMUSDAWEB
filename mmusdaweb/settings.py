from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o34kjnpf$s!c-s#2xxcbv9n8u@auiwr#mz7+k@^*e1ttbol8g('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'church',
    'sorl.thumbnail',
    'whitenoise.runserver_nostatic',
    'upload',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'mmusdaweb.urls'

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

WSGI_APPLICATION = 'mmusdaweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(BASE_DIR / 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'mmusda',
#         'USER': 'postgres',
#         'PASSWORD': '1/1/1999',
#         'HOST': 'localhost',
#         'PORT': '5432',     
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8inin4tva6qtu',
        'USER': 'jbhsaafsfowvpo',
        'PASSWORD': '554338963f453b2c7a67f921b175c5c83e9ad187962500b4fcf64ecabaa90623',
        'HOST': 'ec2-44-205-63-142.compute-1.amazonaws.com',
        'PORT': '5432',     
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

AWS_ACCESS_KEY_ID = 'AKIAWHRPPTJEACWLTCPS'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'mmusdaweb'

AWS_S3_FILE_OVEWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_S3_REGION_NAME = 'Asia Pacific (Tokyo) ap-northeast-1'
AWS_S3_ADDRESSING_STYLE = 'virtual'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# USE_S3 = os.getenv('USE_S3') == 'TRUE'
# USE_S3 = False
#
# if USE_S3:
#     # aws settings
#     AWS_ACCESS_KEY_ID = 'AKIAWHRPPTJEACWLTCPS'
#     AWS_SECRET_ACCESS_KEY = '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'
#     AWS_STORAGE_BUCKET_NAME = 'mmusdaweb'
#     AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' %AWS_STORAGE_BUCKET_NAME
#     AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
#     AWS_DEFAULT_ACL = 'public-read'
#
#     # s3 static Settings
#     STATIC_LOCATION = 'static'
#     STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
#     STATICFILES_STORAGE = 'hello_django.storage_backends.StaticStorage'
#
#     # s3 media settings
#     PUBLIC_MEDIA_LOCATION = 'media'
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
#     DEFAULT_FILE_STORAGE = 'hello_django.storage_backends.PublicMediaStorage'
#
#     PRIVATE_MEDIA_LOCATION = 'private_media'
#     PRIVATE_FILE_STORAGE = 'hello_django.storage_backends.PrivateMediaStorage'
# else:
#     MEDIA_URL = '/media/'
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
#     STATIC_URL = '/static/'
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
#
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# # MEDIA_URL = 'media'
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# # STATICFILES_DIRS = [
# #     (os.path.join(BASE_DIR, 'static'),)
# # ]
#
#
#
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# DEFAULT_FILE_STORAGE = 'core.storages.MediaStore'
# #
# STATICFILES_STORAGE = 'core.storages.S3StaticBucket'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
#
#
