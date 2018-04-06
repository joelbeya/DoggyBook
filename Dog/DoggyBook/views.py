from django.shortcuts import render,redirect
from .models import *
import sys
from django.contrib.auth import logout, get_user
from django.http import *
from django.contrib.auth.hashers import *
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    objets = Chien.objects.order_by('-created_at');
    return render(request, 'dogo/index.html', {'objets':objets})

def requete(request,obj):
    identifier = getattr(sys.modules[__name__], obj)
    objets = identifier.all()
    return render(request, 'dogo/requete.html', {'objets':objets})

def show(request, obj, key):
    identifier = getattr(sys.modules[__name__], obj)
    objet = identifier.find(int(key))
    return render(request, 'dogo/show.html', {'objet':objet})

def subscribe(request):
    mail = request.POST['mail']
    password = make_password(request.POST['password'])
    nom = request.POST['name']
    prenom = request.POST['first_name']
    sexe = request.POST['sexe']
    date_naissance = request.POST['birth']
    
    User.objects.create(mail=mail, password=password, nom=nom, prenom=prenom, sexe=sexe, date_naissance=date_naissance)
    return redirect('/dogo/index')

def log(request):
    try:
        m = User.objects.get(mail=request.POST['mail'])
    except ObjectDoesNotExist:
        return HttpResponse("Your username and password didn't match.")

    if check_password(request.POST['password'], m.password):
        request.session['id'] = m.id
        return redirect('/dogo/index')
    else:
        return HttpResponse("Your username and password didn't match.")

def log_out(request):
    request = HttpRequest()
    engine = import_module(settings.SESSION_ENGINE)
    if self.session:
        request.session = self.session
        request.user = get_user(request)
    else:
        request.session = engine.SessionStore()
    logout(request)
    self.cookies = SimpleCookie() 
