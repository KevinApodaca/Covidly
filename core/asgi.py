# -*- encoding: utf-8 -*-
"""
Covidly Dashboard
Team 2
CS 4390
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
