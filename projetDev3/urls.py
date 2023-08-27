"""
URL configuration for projetDev3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jardins import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name = 'index'),
    path('jardins/', views.jardins , name = 'jardins'),
    path('recherche/', views.recherche , name = 'recherche'),
    path('jardin/ajouter/', views.jardinajouter , name = 'jardinajouter'),
    path('jardin/afficher/<slug:slug>/', views.jardinafficher , name = 'jardinafficher'),
    path('blog/', views.blog , name = 'blog'), # Définir une adresse d'une page http://localhost:8000/blog ('blog/') qui a pour nom (name) 'blog' qui affichera le design de la view blog se trouvant dans le fichier views.py (def blog)
    path('contact/', views.contact , name = 'contact'),
    
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('dashboard/',views.dashboard, name='dashboard'),
]
