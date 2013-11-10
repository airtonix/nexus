from django.conf import settings

MEDIA_PREFIX = getattr(settings, 'NEXUS_STATIC_PREFIX', '/static/nexus/')

if getattr(settings, 'NEXUS_USE_DJANGO_STATIC_URL', False):
    MEDIA_PREFIX = getattr(settings, 'STATIC_URL', MEDIA_PREFIX)
