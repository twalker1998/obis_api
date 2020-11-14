__author__ = 'Mark Stacy'
import os
import ssl
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

appname = "obis" 
#****** Application Settings *******************************************************
Page_Title = 'OBIS API'
Application_Title = 'Oklahoma Biodiversity Information System'
#****** Django Settings  ***********************************************************

SECRET_KEY = '(This is a secret key. Update key to secure api)'
# SCRIPT_NAME Override, I had difficulty setting up NGINX settings
# proxy_set_header SCRIPT_NAME /api; # Not working in config. Temporary fix by add
# FORCE_SCRIPT_NAME in Django settings.py
# If None will default back to Nginx config.
FORCE_SCRIPT_NAME= '/api/'

#Behind reverse proxy set header to trust for https
#replace values in next two lines with commented text if https is needed and behind proxy
USE_X_FORWARDED_HOST = False  # True
SECURE_PROXY_SSL_HEADER = None  # ('HTTP_X_FORWARDED_PROTO', 'https')

#NGINX EXAMPLE for https
#   location  /api/ {
#           add_header 'Access-Control-Allow-Origin' '*';
#           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#           proxy_set_header Host $http_host;
#           proxy_set_header X-Forwarded-Proto 'https';
#           proxy_pass http://0.0.0.0:8080/ ;
#    }
# From above Access-Control-Allow-Origin is used to enable cross-orgin resource sharing(CORS)
# Many different configurations - 'Access-Control-Allow-Origin' '*' allows all hosts. Please
# check the docs depending on web server used. This example is for Nginx!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['obis.ou.edu', 'obis.twalk.tech']
# Cookie Domain
# Domain cookie. Can overide for subdomains ie. ".example.com"  (note the leading dot!)
# for cross-domain cookies, or use None for a standard domain cookie.
SESSION_COOKIE_DOMAIN =None
CSRF_COOKIE_DOMAIN = None

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'obis':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST':'10.27.192.243',
        'NAME': 'obis',
        'USER': 'mstacy',
        'PASSWORD': '1969obis2032',
    },
}

DATABASE_ROUTERS = ['obis.database_router.obisRouter',]
#******* Queue  *******************************************************

MEMCACHE_HOST = "cybercom_memcache"
MEMCACHE_PORT = 11211

MONGO_HOST = "cybercom_mongo"
MONGO_PORT = 27017 
MONGO_DB = "obis"
MONGO_LOG_COLLECTION = "task_log"
MONGO_TOMBSTONE_COLLECTION = "tombstone"

BROKER_URL = 'amqp://bkobis:dhY7GFEW12@cybercom_rabbitmq:5671/obis'
BROKER_USE_SSL = {
  'keyfile': '/ssl/client/key.pem',
  'certfile': '/ssl/client/cert.pem',
  'ca_certs': '/ssl/testca/cacert.pem',
  'cert_reqs': ssl.CERT_REQUIRED
}


CELERY_RESULT_BACKEND = 'mongodb://bkobis:dhY7GFEW12@cybercom_mongo:27017/?ssl=true&ssl_ca_certs=/ssl/testca/cacert.pem&ssl_certfile=/ssl/client/mongodb.pem' 
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": MONGO_DB,
    "taskmeta_collection": MONGO_TOMBSTONE_COLLECTION
}

#******* Catalog ******************************************************
CATALOG_EXCLUDE = ['admin','local','cybercom_auth','system.users','default_collection','obis']
CATALOG_INCLUDE = ['catalog']
CATALOG_URI = 'mongodb://bkobis:dhY7GFEW12@cybercom_mongo:27017/?ssl=true&ssl_ca_certs=/ssl/testca/cacert.pem&ssl_certfile=/ssl/client/mongodb.pem'
CATALOG_ANONYMOUS=True
#*********** Data Store ************************************************
DATA_STORE_EXCLUDE = ['admin','local','cybercom_auth','system.users','catalog','default_collection','obis',]
DATA_STORE_MONGO_URI = 'mongodb://bkobis:dhY7GFEW12@cybercom_mongo:27017/?ssl=true&ssl_ca_certs=/ssl/testca/cacert.pem&ssl_certfile=/ssl/client/mongodb.pem'
DATA_STORE_ANONYMOUS=True
#*********** DOCKER_HOST_DATA_DIRECTORY ********************
DOCKER_HOST_DATA_DIRECTORY = "/opt/obis"
#*********** Email Configuration ********************
# Uncomment and configure to enable send email
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'username'
#EMAIL_HOST_PASSWORD = 'password'
#EMAIL_USE_TLS = True

