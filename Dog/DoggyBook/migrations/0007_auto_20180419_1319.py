# Generated by Django 2.0.3 on 2018-04-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoggyBook', '0006_auto_20180418_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='model_pic',
            field=models.ImageField(default='DoggyBook/Dog/media/photos/chien/dogo5.jpeg', upload_to='photos/user/'),
        ),
    ]