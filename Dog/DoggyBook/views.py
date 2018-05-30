from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect
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
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import ImageUploadForm, ImageUploadForm_chien, ImageUploadForm_user
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView


# Pour l'image dans le rapport

def index(request):
    objets = Chien.objects.order_by('-created_at');
    return render(request, 'DoggyBook/index.html', {'objets':objets})



def upload_pic_chien(request,key):
    if request.method == 'POST':
        form = ImageUploadForm_chien(request.POST, request.FILES)
        if form.is_valid():
            c = Chien.objects.get(id=int(key))
            c.photo_profil = form.cleaned_data['image']
            c.save()
            a = '/doggybook/chien/' + str(c.id)
            return redirect(a)
    return HttpResponseForbidden('allowed only via POST')



def upload_pic_user(request):
    if request.method == 'POST':
        form = ImageUploadForm_user(request.POST, request.FILES)
        if form.is_valid():
            u = request.user.proprio
            u.photo_profil = form.cleaned_data['image']
            u.save()
            a = 'profil/' + str(request.user.id)
            return redirect(a)
    return HttpResponseForbidden('allowed only via POST')



def photoChien(request, key):
    objets = Chien.objects.photos(id=int(key))
    return render(request,'DoggyBook/lightbox.html', {'objets':objets})





def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Photo()
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload succesS')
    return HttpResponseForbidden('allowed only via POST')




def gestionMembre(request):
    objets = Chien.objects.all()
    return render(request, 'DoggyBook/gestionMembre.html', {'objets':objets})


def requete(request,obj):
    identifier = getattr(sys.modules[__name__], obj)
    objets = identifier.all()
    return render(request, 'DoggyBook/requete.html', {'objets':objets})


# def show(request, obj, key):
#     identifier = getattr(sys.modules[__name__], obj)
#     objet = identifier.find(int(key))
#     return render(request, 'DoggyBook/show.html', {'objet':objet})


@login_required(login_url='/doggybook')
def user(request, key):
    objet = User.objects.get(id=int(key))
    chiens = objet.proprio.chiens.all()
    return render(request, 'DoggyBook/profil.html', {'objet':objet,'chiens':chiens})

def race(request):
    objets = Race.all()
    return render(request, 'DoggyBook/race.html', {'objets':objets})

def chien(request,key):
    objet = Chien.objects.get(id=int(key))
    return render(request, 'DoggyBook/chien.html', {'objet':objet,'key':key})


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
    tel = request.POST['tel']

    try:
        u = User.objects.get(email=mail)
        return redirect('/doggybook')
    except User.DoesNotExist:
        u = None
        u = User.objects.create_user(username=mail, email=mail, first_name=prenom, last_name=nom, password=password)
        Proprietaire.objects.create(user=u, date_naissance = date_naissance, sexe=sexe, telephone=tel)

    return redirect('/doggybook/index')
    #
    # if User.objects.get(email=mail) is not None:
    #     u = User.objects.create_user(username=mail, email=mail, first_name=prenom, last_name=nom, password=password)
    #     Proprietaire.objects.create(user=u, date_naissance = date_naissance, sexe=sexe)
    # else:
    #     User.objects.create_user(username=mail, email=mail, first_name=prenom, last_name=nom, password=password)

@login_required(login_url='/doggybook')
def ajoutC(request):
    race = Race.all().order_by('nom')
    pere = Chien.objects.filter(sexe='M').order_by('nom')
    mere = Chien.objects.filter(sexe='F').order_by('nom')
    chiens = request.user.proprio.chiens.filter()
    return render(request, 'DoggyBook/ajout_chien.html',{'race':race, 'pere':pere, 'mere':mere, 'chiens':chiens})

@login_required(login_url='/doggybook')
def ajoutChien(request):
    nom = request.POST['nom']
    date_naissance = request.POST['birth']
    couleur_poils = request.POST['poils']
    couleur_yeux = request.POST['yeux']
    if (request.POST['sexe']=="Male"):
        sexe = 'M'
    else:
        sexe = 'F'

    proprio = request.user.proprio
    race = Race.objects.get(id=int(request.POST['race']))
    if (request.POST['pere'] != "None"):
        pere = Chien.objects.get(id=int(request.POST['pere']))
    else:
        pere = None
    if (request.POST['mere'] != "None"):
        mere = Chien.objects.get(id=int(request.POST['mere']))
    else:
        mere = None
    c = Chien.objects.create(nom=nom,date_naissance=date_naissance,couleur_poils=couleur_poils,couleur_yeux=couleur_yeux,sexe=sexe,proprio=proprio,race=race,pere=pere,mere=mere)

    txt='/doggybook/profil/' + str(request.user.id)
    return redirect(txt)


@login_required(login_url='/doggybook')
def modifP(request):
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    date_naissance = request.POST['birth']
    tel = request.POST['tel']
    u = request.user
    p = u.proprio
    u.last_name=nom
    u.first_name=prenom
    p.date_naissance=date_naissance
    p.telephone=tel
    u.save()
    p.save()

    txt='/doggybook/profil/' + str(u.id)
    return redirect(txt)

@login_required(login_url='/doggybook')
def modifC(request):
    nom = request.POST['nom']
    date_naissance = request.POST['birth']
    couleur_poils = request.POST['poils']
    couleur_yeux = request.POST['yeux']
    if (request.POST['pere'] != "None"):
        pere = Chien.objects.get(id=int(request.POST['pere']))
    else:
        pere = None
    if (request.POST['mere'] != "None"):
        mere = Chien.objects.get(id=int(request.POST['mere']))
    else:
        mere = None

    c = Chien.objects.get(id=int(request.POST['id']))
    c.nom = nom
    c.date_naissance=date_naissance
    c.couleur_poils=couleur_poils
    c.couleur_yeux=couleur_yeux
    c.mere=mere
    c.pere=pere
    c.save()

    txt='/doggybook/profil/' + str(request.user.id)
    return redirect(txt)

@login_required(login_url='/doggybook')
def supprC(request):
    c = Chien.objects.get(id=int(request.POST['idC']))
    c.delete()

    txt='/doggybook/profil/' + str(u.id)
    return redirect(txt)

def log(request):
    username = request.POST['mail']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/doggybook/index')
    else:
        #raise HttpResponse("Your username and password didn't match.")
        return redirect('/doggybook/index')

@login_required(login_url='/doggybook')
def log_out(request):
    logout(request)
    return redirect('/doggybook/index')

def arbre(request,key):
    objet = Chien.objects.get(id=int(key))
    return render(request,'DoggyBook/genealogie.html', {'objet':objet})

def arbres(request,key):
    objet = Chien.objects.get(id=int(key))
    fraternite = Chien.objects.filter(pere=objet.pere,mere=objet.mere).exclude(id=objet.id)
    if(objet.sexe == "M"):
        enfants = Chien.objects.filter(pere=objet)
    else:
        enfants = Chien.objects.filter(mere=objet)
    return render(request,'DoggyBook/gene.html', {'objet':objet,'fraternite':fraternite,'enfants':enfants})



# def gallery(request, key):
#     list = photos.objects.all()
#     paginator = Paginator(list, 10)
#
#     page = request.GET.get('page')
#     try:
#         albums = paginator.page(page)
#     except PageNotAnInteger:
#         albums = paginator.page(1)
#     except EmptyPage:
#         albums = paginator.page(paginator.num_pages)
#
#     return render(request, 'gallery.html', { 'albums': list })

# class AlbumDetail(DetailView):
#      model = Photo

def get_context_data(request, key):
         objet = Photo.objects.get(id=int(key))
         chiens = objet.chien.model_pic.all()
         return render(request, 'DoggyBook/album_detail.html', {'objet':objet,'chiens':chiens})


    #  def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(photos, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the images
    #     context['images'] = photos.objects.get(album=self.object.id)
    #     return context

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)
