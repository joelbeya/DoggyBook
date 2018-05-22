# Generated by Django 2.0.2 on 2018-04-12 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DoggyBook', '0003_auto_20180412_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='photos/chien/')),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='chien',
            name='avis',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='chien',
            name='photo_profil',
            field=models.ImageField(blank=True, upload_to='photos/profilchien/'),
        ),
        migrations.AddField(
            model_name='proprietaire',
            name='photo_profil',
            field=models.ImageField(blank=True, upload_to='photos/proprio/'),
        ),
        migrations.AddField(
            model_name='race',
            name='photo_profil',
            field=models.ImageField(blank=True, upload_to='photos/race/'),
        ),
        migrations.AlterField(
            model_name='chien',
            name='sexe',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='sexe',
            field=models.CharField(max_length=1),
        ),
        migrations.AddField(
            model_name='chien',
            name='photos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='DoggyBook.Photo'),
        ),
    ]