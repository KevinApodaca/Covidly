from django.urls import path, re_path
from app import views
"""
Documentation will go here, eventually. Sebastian will write it.
"""
urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
]
