# Generated by Django 2.0.5 on 2018-05-27 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DoggyBook', '0005_merge_20180527_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='chien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='DoggyBook.Chien'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='model_pic',
            field=models.ImageField(blank=True, default='DoggyBook/Dog/media/photos/chien/dogo5.jpeg', null=True, upload_to='photos/user/'),
        ),
    ]
