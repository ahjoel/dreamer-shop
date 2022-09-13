
# SECURITY WARNING: keep the secret key used in production secret!
from decouple import config
import dj_database_url
from django.conf.global_settings import DATABASES

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dreamer-shop.herokuapp.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES['default'] = dj_database_url.config()

