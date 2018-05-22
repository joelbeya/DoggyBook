from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .models import *


app_name='DoggyBook'

urlpatterns = [

	# Cette instruction qui nous intersse ici
	url(r'^$', views.index, name='index'),
	# Pour l'image dans le rapport 
	url(r'^upload_pic$', views.upload_pic, name = 'upload_pic'),
	url(r'^upload_pic_user$', views.upload_pic_user, name = 'upload_pic_user'),
	url(r'^upload_pic_chien$', views.upload_pic_chien, name = 'upload_pic_chien'),
	url(r'^photo/',TemplateView.as_view(template_name = 'photo.html')),
	url(r'^index', views.index,name='index'),
	url(r'^subscribe', views.subscribe),
	url(r'^gestionMembre$', views.gestionMembre, name='gestionMembre'),
	url(r'^ajoutChien', views.ajoutChien),
	url(r'^login', views.log),
	url(r'^logout', views.log_out),
	url(r'^album/(?P<key>[0-9]*)$', views.photoChien),
	url(r'^race/(?P<key>[0-9]*)$', views.race),
	url(r'^chien/(?P<key>[0-9]*)$', views.chien),
	#url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
	url(r'^profil/(?P<key>[0-9]*)$', views.user),
   	url(r'^(?P<obj>[A-Za-z]*)$', views.requete),
]
