from django.urls import re_path

from . import views

#name space des urls de l'application
app_name='activities'

urlpatterns = [
    re_path(r'ies/$', views.index, name='index'),
]
