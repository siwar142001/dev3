from django import forms 
from jardins.models import Jardin    
from jardins.models import Avis



class JardinForm ( forms.ModelForm):    
    class Meta:
        model = Jardin
        fields = ['nom', 'description', 'adresse', 'code_postal', 'tel', 'email', 'site']
        
    nom = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nom *'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description *'}))
    adresse = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Adresse *'}))
    code_postal = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Code postal *'}))
    tel = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Téléphone *'}))
    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email*'}))
    site = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Site web *'}))
   

class AvisForm(forms.ModelForm):    
    class Meta:
        model = Avis
        fields = ['jardin', 'nom_parent', 'email_parent', 'tel_parent', 'espace', 'proprete', 'localisation', 'prix', 'service', 'contenu']

    PROPRETE_CHOICES = (
        (0, 'Aucune étoile'),
        (1, '1 étoile'),
        (2, '2 étoiles'),
        (3, '3 étoiles'),
        (4, '4 étoiles'),
        (5, '5 étoiles'),
    ) 
     
    proprete = forms.ChoiceField(choices=PROPRETE_CHOICES, widget=forms.Select())
    contenu = forms.CharField(widget=forms.Textarea())    
    email_parent = forms.EmailField(widget=forms.EmailInput()) 

    def __init__(self, jardin_en_cours, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jardin'].initial = jardin_en_cours
        #self.fields['jardin'].widget = forms.HiddenInput()  # Set jardin field widget to HiddenInput
    
class ContactForm(forms.Form):
    lastname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nom *'}))
    firstname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Prénom *'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email *'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Téléphone *'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message *'}))
    
  