"""
WSGI config for BetoGame project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from .generalsetting import NAME_PROYECT
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", NAME_PROYECT+".settings")

application = get_wsgi_application()
