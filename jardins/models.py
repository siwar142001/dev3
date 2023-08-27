from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Ville (BaseModel):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique = True , null = True , blank = True)
    code_postal = models.CharField(max_length=4)
    image = models.ImageField(upload_to="staticfiles/front/img/villes", null = True)
    accueil = models.IntegerField(default=0)
       
    
class Caracteristique (BaseModel):
    nom = models.CharField(max_length=100)
    icone = models.CharField(max_length=60)    # class CSS de l'icone a partir de font awesome  

class Proprietaire (BaseModel):
    nom = models.CharField(max_length=100, null = False)
    prenom = models.CharField(max_length=100, null = False)  
    email = models.EmailField( null = False) 
    mdp = models.CharField(max_length=100, null = False )    
    
class Jardin (BaseModel):
    nom = models.CharField(max_length=200) 
    slug = models.SlugField(unique = True , null = True , blank = True)
    description = models.TextField(null = True) 
    adresse = models.CharField(max_length=200 , null = True) 
    code_postal = models.CharField(max_length=4 , null = True)
    ville = models.ForeignKey(Ville , on_delete=models.CASCADE , related_name = "villes" )
    tel = models.CharField(max_length=100 , null = True) 
    email = models.CharField(max_length=100 , null = True) 
    site = models.CharField(max_length=100 , null = True) 
    logo = models.ImageField(upload_to="staticfiles/front/img/logos" , null = True)
    proprietaire = models.ForeignKey(User , on_delete=models.CASCADE )
    caracteristiques = models.ManyToManyField(Caracteristique) 
    
class JardinImage (BaseModel):
    jardin = models.ForeignKey(Jardin , on_delete=models.CASCADE , related_name = "jardin_images" ) # !!!!!!! related_name c'est ce qu'on va utiliser dans 
    image = models.ImageField(upload_to="staticfiles/front/img/jardins")
    couverture = models.IntegerField(default=0)
    
class Avis (BaseModel):
    jardin = models.ForeignKey(Jardin , on_delete=models.CASCADE , related_name = "jardin_avis" )
    
    contenu = models.CharField(max_length=200, null = True) # description non obligatoire
    
    espace = models.IntegerField(default=0, null = False) # note de 1 à 5 - null = False c-a-d obligatoire
    proprete = models.IntegerField(default=0, null = False) # de 1 à 5
    localisation = models.IntegerField(default=0, null = False) # de 1 à 5
    prix = models.IntegerField(default=0, null = False) # de 1 à 5
    service = models.IntegerField(default=0, null = False) # de 1 à 5
    nb_etoiles = models.IntegerField(default=0, null = False) # de 1 à 5
    
    nom_parent = models.CharField(max_length=200, null = True) # nom et prénom du parent obligatoire
    email_parent = models.CharField(max_length=200, null = True) # email du parent obligatoire
    tel_parent = models.CharField(max_length=200, null = False) # tel du parent obligatoire