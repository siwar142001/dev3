# Generated by Django 4.2.3 on 2023-08-12 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristique',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=100)),
                ('icone', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jardin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('code_postal', models.CharField(max_length=4, null=True)),
                ('tel', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('site', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(null=True, upload_to='staticfiles/front/img/logos')),
                ('caracteristiques', models.ManyToManyField(to='jardins.caracteristique')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('code_postal', models.CharField(max_length=4)),
                ('image', models.ImageField(null=True, upload_to='staticfiles/front/img/villes')),
                ('accueil', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JardinImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='staticfiles/front/img/jardins')),
                ('couverture', models.IntegerField(default=0)),
                ('jardin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jardin_images', to='jardins.jardin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jardin',
            name='proprietaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proprietaires', to='jardins.proprietaire'),
        ),
        migrations.AddField(
            model_name='jardin',
            name='ville',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villes', to='jardins.ville'),
        ),
    ]
