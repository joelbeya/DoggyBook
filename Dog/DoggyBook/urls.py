from django.conf.urls import url
from . import views
from .models import *

app_name='DoggyBook'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index,name='index'),
	url(r'^subscribe', views.subscribe),
	url(r'^login', views.log),
	url(r'^logout', views.log_out),
    url(r'^(?P<obj>[A-Za-z]*)$', views.requete),
    url(r'^(?P<obj>[A-Za-z]*)/(?P<key>[0-9]*)$', views.show),
]
