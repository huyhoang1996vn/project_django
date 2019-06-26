from settings import *

# websites/manage.py runserver --settings=config.local
print '>>>>>>>>> DEPLOY IN LOCAL'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'lands_web',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

DEFAULT_TO_ADMIN_EMAIL = "contact@metiz.vn"
DEFAULT_FROM_EMAIL = "VocSach Service <no-reply@vocsach.vn>"
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# https://app.sendgrid.com/
'''
    Step 1: add your domain to sender authentication
    Step 2: in your domain, add subdomain from step 1
    Step 3: Set default for subdomain created

'''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True



