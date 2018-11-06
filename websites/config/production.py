from settings import *

 # websites/manage.py runserver --settings=config.production
print '>>>>>>>>>   DEPLOY IN PRODUCTION'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'production_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}