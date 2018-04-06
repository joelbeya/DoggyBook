from django.db import models
from django.conf import settings


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



class Proprietaire(SuperClass):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null=True)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    sexe = models.BooleanField()



class Chien(SuperClass):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    couleur_poils = models.CharField(max_length=255)
    couleur_yeux = models.CharField(max_length=255)
    sexe = models.BooleanField()
    proprio = models.ForeignKey(Proprietaire,on_delete=models.CASCADE)
    race = models.ForeignKey(Race,on_delete=models.CASCADE)
    pere = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='enfant_pere')
    mere = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='enfant_mere')