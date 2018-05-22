# Generated by Django 2.0.2 on 2018-04-06 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('sexe', models.BooleanField()),
                ('mere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enfant_mere', to='DoggyBook.Chien')),
                ('pere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enfant_pere', to='DoggyBook.Chien')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255, null=True)),
                ('date_naissance', models.DateField()),
                ('adresse', models.CharField(max_length=255)),
                ('sexe', models.BooleanField()),
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chien',
            name='proprio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoggyBook.Proprietaire'),
        ),
        migrations.AddField(
            model_name='chien',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoggyBook.Race'),
        ),
    ]