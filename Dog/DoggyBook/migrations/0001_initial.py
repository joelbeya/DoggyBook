<<<<<<< HEAD
=======
# Generated by Django 2.0.4 on 2018-05-25 17:12
# Generated by Django 2.0.2 on 2018-05-25 17:21


>>>>>>> 05453980459ece05e949c5e3a1f08b2de0a7ca58
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('couleur_poils', models.CharField(max_length=255)),
                ('couleur_yeux', models.CharField(max_length=255)),
                ('sexe', models.CharField(max_length=1)),
                ('photo_profil', models.ImageField(blank=True, default='dog_default_profil_pic.png', upload_to='photos/profilchien/')),
                ('avis', models.TextField(blank=True)),
                ('mere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enfant_mere', to='DoggyBook.Chien')),
                ('pere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enfant_pere', to='DoggyBook.Chien')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='DoggyBook/Dog/media/photos/chien/dogo5.jpeg', upload_to='photos/user/')),
                ('chien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='DoggyBook.Chien')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_naissance', models.DateField()),
                ('adresse', models.CharField(max_length=255)),
                ('sexe', models.CharField(max_length=1)),
                ('photo_profil', models.ImageField(blank=True, default='user_default_profil_pic.jpg', upload_to='photos/proprio')),
                ('telephone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proprio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('taille', models.IntegerField()),
                ('morphologie', models.CharField(max_length=255)),
                ('comportement', models.CharField(max_length=255)),
                ('photo_profil', models.ImageField(blank=True, upload_to='photos/race/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chien',
            name='proprio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chiens', to='DoggyBook.Proprietaire'),
        ),
        migrations.AddField(
            model_name='chien',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chiens', to='DoggyBook.Race'),
        ),
    ]
