# -*- encoding: utf-8 -*-
"""
Covidly Dashboard
Team 2
CS 4390
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processdata.urls')),
    path('', include('app.urls')),  # add this
]
