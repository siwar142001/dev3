# Generated by Django 4.2.3 on 2023-08-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardins', '0002_avis'),
    ]

    operations = [
        migrations.AddField(
            model_name='avis',
            name='nb_etoiles',
            field=models.IntegerField(default=0),
        ),
    ]