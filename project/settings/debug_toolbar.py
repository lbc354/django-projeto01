from .installed_apps import INSTALLED_APPS
from .middlewares import MIDDLEWARE

INSTALLED_APPS += ['debug_toolbar',]
# pode ser feito das duas formas
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',] + MIDDLEWARE

# Django Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]