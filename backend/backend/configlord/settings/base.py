import environ
from os import path
import pathlib

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
project_root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),)
CURRENT_ENV = 'dev' # 'dev' is the default environment
FRONTEND_ROOT=path.join(pathlib.Path(BASE_DIR).parents[2], 'frontend')
print(FRONTEND_ROOT)
# read the .env file associated with the settings that're loaded
env.read_env('backend/configlord/{}.env'.format(CURRENT_ENV))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = '!xki!ps8tf2p*i92=_gv(2qriniys*gj)e)(ah=)$v540%_u+='
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'main',
    'games',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'backend.wsgi.application'

ROOT_URLCONF = 'backend.urls'

STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [
    FRONTEND_ROOT, path.join(FRONTEND_ROOT, 'dist','static')
]
print (path.join(FRONTEND_ROOT, 'dist','static'))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_ROOT],
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

ALLOWED_HOSTS = ['192.168.1.63', '127.0.0.1', '192.168.1.101', '78.26.210.61']

APPEND_SLASH=False