from django.conf.urls import url
from . import views
from .models import *

app_name='DoggyBook'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index,name='index'),
	url(r'^subscribe', views.subscribe),
	url(r'^gestionMembre$', views.gestionMembre, name='gestionMembre'),
	url(r'^ajoutChien', views.ajoutChien),
	url(r'^login', views.log),
	url(r'^logout', views.log_out),
<<<<<<< HEAD
	#url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
=======
#	url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
>>>>>>> 939c91fee5fa0a07630f95927e872540c15b7dcf
	url(r'^profil/(?P<key>[0-9]*)$', views.user),
    url(r'^(?P<obj>[A-Za-z]*)$', views.requete),
    url(r'^(?P<obj>[A-Za-z]*)/(?P<key>[0-9]*)$', views.show),
]
