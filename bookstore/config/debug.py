from django.conf import settings


def show_toolbar(request):
    return True


DEVELOP_APPS = [
    'debug_toolbar',
]

DEVELOP_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

settings.INSTALLED_APPS += DEVELOP_APPS
settings.MIDDLEWARE += DEVELOP_MIDDLEWARE

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1')
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.timer.TimerPanel',
]

settings.REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
})

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}
