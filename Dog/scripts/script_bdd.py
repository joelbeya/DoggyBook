from DoggyBook.models import *

def run():
	print("Cela va supprimer toute la base de données pour rajouter de nouvelles instances, en êtes-vous sûrs ?")
	input("Appuyez sur une Entrée pour valider")


	"""Proprietaire.objects.all().delete()
	Race.objects.all().delete()
	Chien.objects.all().delete()"""

	#Ajout des Proprios
	u = User.objects.create_user(username="Stanton@test.com",email="Stanton@test.com",first_name="Lani",last_name="Stanton",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1982-07-06",adresse="CP 303, 9196 Orci Ave",sexe="H",telephone="0642158792")

	u = User.objects.create_user(username="Holmes@test.com",email="Holmes@test.com",first_name="Lara",last_name="Holmes",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1938-05-15",adresse="1503 Vel, Avenue",sexe="H",telephone="0647125897")

	u = User.objects.create_user(username="Duran@test.com",email="Duran@test.com",first_name="Amaya",last_name="Duran",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1991-04-26",adresse="9193 Eros Ave",sexe="F",telephone="0687245899")

	u = User.objects.create_user(username="Palmer@test.com",email="Palmer@test.com",first_name="Cheyenne",last_name="Palmer",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1993-11-24",adresse="CP 283, 8229 Curae Route",sexe="F",telephone="0687245899")

	u = User.objects.create_user(username="Koch@test.com",email="Koch@test.com",first_name="Isaiah",last_name="Koch",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1987-06-05",adresse="Appartement 712-2889 Amet, Av.",sexe="H",telephone="0647125897")

	u = User.objects.create_user(username="Anthony@test.com",email="Anthony@test.com",first_name="Candace",last_name="Anthony",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1954-12-23",adresse="Appartement 828-4215 Ut Ave",sexe="F",telephone="0687245899")

	u = User.objects.create_user(username="Welch@test.com",email="Welch@test.com",first_name="Omar",last_name="Welch",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1955-02-22",adresse="CP 461, 2672 Magna Avenue",sexe="H",telephone="0647125897")

	u = User.objects.create_user(username="West@test.com",email="West@test.com",first_name="Louis",last_name="West",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1955-11-20",adresse="8519 Donec Ave",sexe="H",telephone="0647125897")

	u = User.objects.create_user(username="Haney@test.com",email="Haney@test.com",first_name="Aspen",last_name="Haney",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1984-10-04",adresse="141-8057 Ac Av.",sexe="F",telephone="0687245899")

	u = User.objects.create_user(username="Whitney@test.com",email="Whitney@test.com",first_name="Tiger",last_name="Whitney",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1946-04-21",adresse="578-3953 Phasellus Av.",sexe="F",telephone="0687245899")

	u = User.objects.create_user(username="Hines@test.com",email="Hines@test.com",first_name="Heather",last_name="Hines",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1932-07-18",adresse="Appartement 156-6803 Ad Route",sexe="H",telephone="0647125897")

	u = User.objects.create_user(username="Doyle@test.com",email="Doyle@test.com",first_name="Raya",last_name="Doyle",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1938-01-29",adresse="786-8278 Urna. Av.",sexe="H",telephone="0647125897")

	u = User.objects.create_user(username="Leon@test.com",email="Leon@test.com",first_name="Molly",last_name="Leon",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1953-09-11",adresse="4004 Enim. Rd.",sexe="F",telephone="0687245899")

	u = User.objects.create_user(username="Graham@test.com",email="Graham@test.com",first_name="Kaseem",last_name="Graham",password="test")
	Proprietaire.objects.create(user=u,date_naissance="1963-06-11",adresse="922-5445 At Rd.",sexe="F",telephone="0687245899")
<<<<<<< HEAD

=======
>>>>>>> 939c91fee5fa0a07630f95927e872540c15b7dcf
	
	

	#Ajout des Races
	"""Race.objects.create(nom="Justice",taille=119,morphologie="felis",comportement="eu")
	Race.objects.create(nom="Good",taille=43,morphologie="rum",comportement="nunc")
	Race.objects.create(nom="Harper",taille=143,morphologie="dolor",comportement="metus")
	Race.objects.create(nom="Lynch",taille=120,morphologie="mon",comportement="velit")
	Race.objects.create(nom="Frost",taille=151,morphologie="ligula",comportement="Suspendisse")
	Race.objects.create(nom="Thompson",taille=126,morphologie="Duis",comportement="ipsum")
	Race.objects.create(nom="Buchanan",taille=158,morphologie="Donec",comportement="commodo")
	Race.objects.create(nom="Garcia",taille=20,morphologie="Donec",comportement="Suspendisse")
	Race.objects.create(nom="Herrera",taille=149,morphologie="natoque",comportement="Donec")
	Race.objects.create(nom="Berger",taille=120,morphologie="musclé",comportement="agressif")"""

	#Ajout des Chiens
<<<<<<< HEAD
	"""Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=True,proprio=Proprietaire(1),race=Race(1))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(1),race=Race(2))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(2),race=Race(4),pere=Chien(1),mere=Chien(2))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="rouge",sexe=True,proprio=Proprietaire(3),race=Race(8))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(9),race=Race(9))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(3),race=Race(10),pere=Chien(4),mere=Chien(5))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="bleu",couleur_yeux="bleu",sexe=True,proprio=Proprietaire(12),race=Race(7))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(14),race=Race(1))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(5),race=Race(2),pere=Chien(1),mere=Chien(2))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=True,proprio=Proprietaire(6),race=Race(5))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="marron",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(7),race=Race(6))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(8),race=Race(7),pere=Chien(1),mere=Chien(2))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=True,proprio=Proprietaire(10),race=Race(7))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(11),race=Race(7))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(12),race=Race(9),pere=Chien(10),mere=Chien(8))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=True,proprio=Proprietaire(15),race=Race(1))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(17),race=Race(3))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe=False,proprio=Proprietaire(18),race=Race(4),pere=Chien(10),mere=Chien(8))"""
=======
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(1),race=Race(1))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(1),race=Race(2))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(2),race=Race(4),pere=Chien(1),mere=Chien(2))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="rouge",sexe="M",proprio=Proprietaire(3),race=Race(8))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(9),race=Race(9))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(3),race=Race(10),pere=Chien(4),mere=Chien(5))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="bleu",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(12),race=Race(7))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(14),race=Race(1))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(5),race=Race(2),pere=Chien(1),mere=Chien(2))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(6),race=Race(5))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="marron",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(7),race=Race(6))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(8),race=Race(7),pere=Chien(1),mere=Chien(2))
	Chien.objects.create(nom="Medor",date_naissance="2006-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="M",proprio=Proprietaire(10),race=Race(7))
	Chien.objects.create(nom="Toto",date_naissance="2002-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(11),race=Race(7))
	Chien.objects.create(nom="Pet",date_naissance="2008-10-25",couleur_poils="rouge",couleur_yeux="bleu",sexe="F",proprio=Proprietaire(12),race=Race(9),pere=Chien(10),mere=Chien(8))
>>>>>>> 939c91fee5fa0a07630f95927e872540c15b7dcf
