from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

class SuperClass(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    @classmethod
    def all(self):
        return self.objects.all()

    @classmethod
    def find(self, key):
        try:
            return self.objects.filter(pk=key)
        except:
            raise Http404('Google who are you {} ?')

    def __str__(self):
        return self.nom

    class Meta:
        abstract = True




class Race(SuperClass):
    nom = models.CharField(max_length = 255)
    taille = models.IntegerField()
    morphologie = models.CharField(max_length = 255)
    comportement = models.CharField(max_length = 255)
    photo_profil = models.ImageField(upload_to='photos/race/',blank=True)



class Proprietaire(SuperClass):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='proprio')
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1)
    photo_profil = models.ImageField(upload_to='photos/proprio',blank=True,default='user_default_profil_pic.jpg')
    telephone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.last_name



class Chien(SuperClass):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    couleur_poils = models.CharField(max_length=255)
    couleur_yeux = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1)
    photo_profil = models.ImageField(upload_to='photos/profilchien/',blank=True,default='dog_default_profil_pic.png')
    proprio = models.ForeignKey(Proprietaire,on_delete=models.CASCADE,related_name='chiens')
    race = models.ForeignKey(Race,on_delete=models.CASCADE,related_name='chiens')
    pere = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='enfant_pere')
    mere = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='enfant_mere')
    avis = models.TextField(blank=True)


class Photo(models.Model):
    model_pic = models.ImageField(upload_to = 'photos/user/',null=True,blank=True,default = 'DoggyBook/Dog/media/photos/chien/dogo5.jpeg')
    chien = models.ForeignKey(Chien,on_delete=models.SET_NULL,related_name='photos',blank=True,null=True)

class Rental(models.Model):
    """docstring for Rental."""
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
