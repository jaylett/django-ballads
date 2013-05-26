import sys
from django.conf import settings

DATABASES = {
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_ballads',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    },
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

#DB = 'sqlite3'
DB = 'postgresql'

settings.configure(
    DEBUG=True,
    DATABASES = {
        'default': DATABASES[DB]
    },
    INSTALLED_APPS = [
        'django_ballads',
    ],
)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1, failfast=False)
failures = test_runner.run_tests(['django_ballads', ])
if failures:
    sys.exit(failures)
