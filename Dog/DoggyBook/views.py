from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import sys
from django.contrib.auth import logout, get_user
from django.http import *
from django.contrib.auth.hashers import *
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required


from .forms import PhotoForm
from .models import Photo


def index(request):
    objets = Chien.objects.order_by('-created_at');
    return render(request, 'DoggyBook/index.html', {'objets':objets})

def gestionMembre(request):
    objets = Chien.objects.all()
    return render(request, 'DoggyBook/gestionMembre.html', {'objets':objets})


def requete(request,obj):
    identifier = getattr(sys.modules[__name__], obj)
    objets = identifier.all()
    return render(request, 'DoggyBook/requete.html', {'objets':objets})


def show(request, obj, key):
    identifier = getattr(sys.modules[__name__], obj)
    objet = identifier.find(int(key))
    return render(request, 'DoggyBook/show.html', {'objet':objet})


@login_required(login_url='/doggybook')
def user(request, key):
    objet = User.objects.get(id=int(key))
    return render(request, 'DoggyBook/profil.html', {'objet':objet})


def subscribe(request):
    mail = request.POST['mail']
    password = request.POST['password']
    nom = request.POST['name']
    prenom = request.POST['first_name']
    if (request.POST['sexe'] == "Homme"):
        sexe = 'H'
    else:
        sexe = 'F'
    date_naissance = request.POST['birth']

    u = User.objects.create_user(username=mail, email=mail, first_name=prenom, last_name=nom, password=password)
    Proprietaire.objects.create(user=u, date_naissance = date_naissance, sexe=sexe)

    return redirect('/doggybook/index')


def ajoutChien(request):
    nom= request.POST['nom']
    date_naissance= request.POST['DateNais']
    couleur_poils= request.POST['CouleursPo']
    couleur_yeux= request.POST['CouleursYe']
    sexe= request.POST['sexe']
    proprio= request.POST['proprietaire']
    race= request.POST['race']
    pere= request.POST['pere']
    mere= request.POST['mere']
    Chien.objects.create(nom=nom, date_naissance=date_naissance, couleur_poils=couleur_poils, couleur_yeux=couleur_yeux, sexe=sexe, proprio=proprio, race=race, pere=pere, mere=mere)
    return redirect('/doggybook/gestionMembre')

def log(request):
    username = request.POST['mail']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/doggybook/index')
    else:
        return HttpResponse("Your username and password didn't match.")


def log_out(request):
    logout(request)
    return redirect('/doggybook/index')


"""class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)"""

