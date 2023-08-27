from django.contrib import admin

# Register your models here.
from .models import Ville
admin.site.register(Ville)

from .models import Jardin
admin.site.register(Jardin)


from .models import Proprietaire
admin.site.register(Proprietaire)


from .models import Caracteristique
admin.site.register(Caracteristique)

from .models import JardinImage
admin.site.register(JardinImage)

from .models import Avis
admin.site.register(Avis)

