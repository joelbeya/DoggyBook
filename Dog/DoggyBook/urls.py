from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .models import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf.urls import include


app_name='DoggyBook'
admin.autodiscover()

urlpatterns = [


	url(r'^get_context_data/(?P<key>[0-9]*)$', views.get_context_data, name = 'get_context_data'),
	url(r'^$', views.index, name='index'),
	url(r'^upload_pic$', views.upload_pic, name = 'upload_pic'),
	url(r'^upload_pic_user$', views.upload_pic_user, name = 'upload_pic_user'),
	url(r'^upload_pic_chien/(?P<key>[0-9]*)$', views.upload_pic_chien, name = 'upload_pic_chien'),
	url(r'^photo/',TemplateView.as_view(template_name = 'photo.html')),
	url(r'^index', views.index,name='index'),
	url(r'^subscribe', views.subscribe),
	url(r'^gestionMembre$', views.gestionMembre, name='gestionMembre'),
	url(r'^ajoutC$', views.ajoutC),
	url(r'^ajoutChien', views.ajoutChien),
	url(r'^login', views.log),
	url(r'^logout', views.log_out),
	url(r'^album/(?P<key>[0-9]*)$', views.photoChien),
	url(r'^race$', views.race),
	#url(r'^race/(?P<key>[0-9]*)$', views.race),
	url(r'^chien/(?P<key>[0-9]*)$', views.chien),
	url(r'^modifP$', views.modifP),
	url(r'^modifChien$', views.modifC),
	url(r'^supprC$', views.supprC),
	#url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
	url(r'^profil/(?P<key>[0-9]*)$', views.user),
	url(r'^arbre/(?P<key>[0-9]*)$', views.arbre),
	url(r'^arbres/(?P<key>[0-9]*)$', views.arbres),
   	url(r'^(?P<obj>[A-Za-z]*)$', views.requete),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'app.views.handler404'
