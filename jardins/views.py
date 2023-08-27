from jardins.forms import JardinForm
from jardins.forms import AvisForm
from jardins.models import Jardin, Ville , JardinImage , Caracteristique
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from jardins.forms import ContactForm
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


# Create your views here.

def index (request) : 
    villes = Ville.objects.filter(accueil=1)
    villes_all = Ville.objects.all()
    jardins = Jardin.objects.select_related('ville').all()
    return render (request , 'index.html', {'villes':villes, 'villes_all':villes_all, 'jardins':jardins})

def jardins (request) : 
    villes = Ville.objects.all()
    jardins = Jardin.objects.all()
    return render (request , 'jardins.html', {'villes':villes, 'jardins':jardins})

def recherche (request) : 
    villes = Ville.objects.all()
    jardins = Jardin.objects.all()
    v = request.GET.get('v')  
    
    if v:
        jardins = jardins.filter(ville=v)
    
    n = request.GET.get('n')  
    if n:
        jardins = jardins.filter(Q(nom=n))  
    return render (request , 'jardins.html', {'villes':villes, 'jardins':jardins})


def jardinajouter (request) : 
    form = JardinForm() 
    return render (request , 'jardinajouter.html', {'form': form }) 

def dashboard(request): 
    return render(request, 'dashboard.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'inscription.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'inscription.html', {'form': form})
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'connexion.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'connexion.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    logout(request)
    return redirect('/signin')

def jardinafficher (request,slug) :
    
    jardin = get_object_or_404(Jardin, slug=slug)
    images = jardin.jardin_images.all() # récupérer la lsite des images d'un jardin à partir de JardinImage
    caracteristiques = jardin.caracteristiques.all()
    aviss = jardin.jardin_avis.all()
    
    # Déterminer l'image de couverture
    couverture = 'staticfiles/front/img/jardins/couverture-default.jpg'
    for img in images:
        if(img.couverture == 1):
            couverture = img.image
            break 
    espace = 0
    if(len(aviss)): # Si le jardin a au moins un avis
        #Déterminer les notes pour chaque critère et calculer le nombre d'étoiles global
        for avis in aviss:
            espace = espace + avis.espace 
            
        espace = round(espace/len(aviss) )
        espace_pourcentage = espace * 20
    
    service = 0
    if(len(aviss)): # Si le jardin a au moins un avis
        #Déterminer les notes pour chaque critère et calculer le nombre d'étoiles global
        for avis in aviss:
            service = service + avis.service 
            
        service = round(service/len(aviss) )
        service_pourcentage = service * 20
        
    localisation = 0
    if(len(aviss)): # Si le jardin a au moins un avis
        #Déterminer les notes pour chaque critère et calculer le nombre d'étoiles global
        for avis in aviss:
            localisation = localisation + avis.localisation 
            
        localisation = round(localisation/len(aviss) )
        localisation_pourcentage = localisation * 20    
    
    proprete = 0
    if(len(aviss)): # Si le jardin a au moins un avis
        #Déterminer les notes pour chaque critère et calculer le nombre d'étoiles global
        for avis in aviss:
            proprete = proprete + avis.proprete 
            
        proprete = round(proprete/len(aviss))
        proprete_pourcentage = proprete * 20
    
    prix = 0
    if(len(aviss)): # Si le jardin a au moins un avis
        #Déterminer les notes pour chaque critère et calculer le nombre d'étoiles global
        for avis in aviss:
            prix = prix + avis.prix 
            
        prix = round(prix/len(aviss) )
        prix_pourcentage = round(prix * 20)
        
    nb_etoiles = (prix + proprete + localisation + service + espace) / 5 #  
    integer_nb_etoiles = int(nb_etoiles)
    
    
    etoiles = ''
    for i in range(round(nb_etoiles)):
        etoiles = etoiles + '<i class="fa fa-star"></i>'
        
        
    message = ''   
        
    #Formulaire d'ajout d'avis
    if request.method == 'POST':
        form_avis = AvisForm(request.POST)
        if form_avis.is_valid():
            form_avis.save()
            aviss = jardin.jardin_avis.all()
            message = "L'avis a été ajouté avec succès"
            #return redirect('jardinafficher', )  # Redirige vers une vue listant les avis
    else:
        form_avis = AvisForm(jardin_en_cours=jardin)
        
    context = {
        'jardin':jardin , 
        'caracteristiques':caracteristiques,
        'images': images, #'images' c'est le nom a utiliser dans jardinafficher.html et images en bleu c'est la variable de la ligne d'avant 
        'couverture': couverture,
        'aviss': aviss,
        'nb_avis': len(aviss),
        'nb_etoiles': nb_etoiles,
        'etoiles': etoiles,
        'proprete': proprete,
        'proprete_pourcentage': proprete_pourcentage,
        'prix': prix,
        'prix_pourcentage': prix_pourcentage,
        'form_avis': form_avis,
        "message": message,
        "localisation": localisation,
        "service": service,
        "espace": espace,
        "integer_nb_etoiles":integer_nb_etoiles,
        "localisation_pourcentage":localisation_pourcentage,
        "service_pourcentage":service_pourcentage, 
        "espace_pourcentage":espace_pourcentage,
        
        
        
    }
    return render(request, 'jardinafficher.html', context)



def blog (request) : 
    return render (request , 'blog.html') 

def contact(request): 
    # Puisqu'on travail en local le message ne sera pas envoyé et un message d'erreur sera affiché. Par contre le problème n'existe pas en version hébérgé car les hébergeurs fournissement par défaut un seerveur SMTP (serveur d'envoi de messagerie)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            send_mail(
                f'Demande de contact',
                f'Name: {firstname} {firstname}\nEmail: {email}\nMessage:\n{message}',
                'selmisiwar3@gmail.com',  # Use your own email address here
                ['m.blaghgi@gmail.com'],  # Recipient's email address
                fail_silently=False,
            )
            success_message = 'Yotre message a été envoyé avec succès. Nous vous répondrons dans les plus brefs délais.'
            return JsonResponse({'success': True, 'message': success_message})
        else:
            error_message = "Une erreur est survenue lors de l'envoi du message."
            return JsonResponse({'success': False, 'message': error_message})
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)



