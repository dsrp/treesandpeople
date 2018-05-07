import environ

from .common import *  # noqa

# set default values and casting
env = environ.Env(DEBUG=(bool, False),)

# False if not in os.environ
DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

SECRET_KEY = env('DJANGO_SECRET_KEY')

# Cached template loader
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#     ('django.template.loaders.cached.Loader', [
#         'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
# ]

# Raven
import os  # noqa
import raven  # noqa

INSTALLED_APPS += [  # noqa
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': env('RAVEN_DSN'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(
        os.path.abspath(os.path.join(BASE_DIR, os.pardir))  # noqa
    ),
}
