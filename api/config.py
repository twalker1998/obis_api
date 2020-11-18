__author__ = 'Tyler Walker' # twalker1998@gmail.com

import os
import ssl

# ************ Application Settings ************
appName          = 'obis'
pageTitle        = 'OBIS API'
applicationTitle = 'Oklahoma Biodiversity Information System'

# ************ Django Settings ************
BASE_DIR          = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS     = ['obis.ou.edu', 'obis.twalk.tech']
SECRET_KEY        = 'w4dr^thkfn9h!1)=h%0*wm1)xy^ezgpp*)(+qwm$xog&2*(1$%'
FORCE_SCRIPT_NAME = '/api/'
SITE_ID           = 1

# Behind reverse proxy, set header to trust for https
# Replace values in next two lines with commented text if https is needed and behind proxy
USE_X_FORWARDED_HOST    = False # True
SECURE_PROXY_SSL_HEADER = None # ('HTTP_X_FORWARDED_PROTO', 'https')

# NGINX EXAMPLE for https
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
DEBUG          = True
TEMPLATE_DEBUG = True

# Cookie Domain
# Domain cookie. Can overide for subdomains ie. ".example.com"  (note the leading dot!)
# for cross-domain cookies, or use None for a standard domain cookie.
SESSION_COOKIE_DOMAIN = None
CSRF_COOKIE_DOMAIN    = None

# Database connection
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   os.path.join(BASE_DIR, 'db.sqlite3')
    },
    'obis': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'HOST':     '10.27.192.243',
        'NAME':     'obis',
        'USER':     '**obis-db-user**',
        'PASSWORD': '**obis-db-pass**'
    }
}

DATABASE_ROUTERS = ['obis.database_router.obisRouter']

# ************ Queue ************
MEMCACHE_HOST = 'cybercom_memcache'
MEMCACHE_PORT = 11211

MONGO_HOST                 = 'cybercom_mongo'
MONGO_PORT                 = 27017
MONGO_DB                   = 'obis'
MONGO_LOG_COLLECTION       = 'task_log'
MONGO_TOMBSTONE_COLLECTION = 'tombstone'

BROKER_URL     = 'amqp://bkobis:dhY7GFEW12@cybercom_rabbitmq:5671/obis'
BROKER_USE_SSL = {
    'keyfile':   '/ssl/client/key.pem',
    'certfile':  '/ssl/client/cert.pem',
    'ca_certs':  '/ssl/testca/cacert.pem',
    'cert_reqs': ssl.CERT_REQUIRED
}

CELERY_RESULT_BACKEND           = 'mongodb://bkobis:**bkobis-pass**@cybercom_mongo:27017/?ssl=true&ssl_ca_certs=/ssl/testca/cacert.pem&ssl_certfile=/ssl/client/mongodb.pem' 
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database":            MONGO_DB,
    "taskmeta_collection": MONGO_TOMBSTONE_COLLECTION
}

# ************ Catalog ************
CATALOG_EXCLUDE   = ['admin','local','cybercom_auth','system.users','default_collection','obis']
CATALOG_INCLUDE   = ['catalog']
CATALOG_URI       = 'mongodb://bkobis:**bkobis-pass**@cybercom_mongo:27017/?ssl=true&ssl_ca_certs=/ssl/testca/cacert.pem&ssl_certfile=/ssl/client/mongodb.pem'
CATALOG_ANONYMOUS = True

# ************ Data Store ************
DATA_STORE_EXCLUDE   = ['admin','local','cybercom_auth','system.users','catalog','default_collection','obis',]
DATA_STORE_MONGO_URI = 'mongodb://bkobis:**bkobis-pass**@cybercom_mongo:27017/?ssl=true&ssl_ca_certs=/ssl/testca/cacert.pem&ssl_certfile=/ssl/client/mongodb.pem'
DATA_STORE_ANONYMOUS = True

# ************ Docker ************
DOCKER_HOST_DATA_DIRECTORY = "/opt/obis"

# ************ Email Configuration ************
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_HOST_USER     = '**noreply-email-user**'
EMAIL_HOST_PASSWORD = '**noreply-email-pass**'
EMAIL_USE_TLS       = True
