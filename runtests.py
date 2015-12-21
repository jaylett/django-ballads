from __future__ import print_function
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

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

settings.configure(
    DEBUG=True,
    INSTALLED_APPS = [
        'django_ballads',
    ],
    DATABASES = {
        'default': DATABASES['sqlite3'],
    },
)
django.setup()
TestRunner = get_runner(settings)

# after we have some settings
from django.test.utils import override_settings

def run_against(db):
    @override_settings(DATABASES = { 'default': DATABASES[db] })
    def run_tests():
        print ("Running tests against %s database." % db)

        test_runner = TestRunner(verbosity=1, failfast=False)
        failures = test_runner.run_tests(['django_ballads', ])
        if failures:
            sys.exit(failures)
    run_tests()

for db in DATABASES.keys():
    run_against(db)
