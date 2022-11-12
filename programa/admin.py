from django.contrib import admin

from .models import centro_Formacion
from .models import programa_Formacion


# Register your models here.

admin.site.register(centro_Formacion)
admin.site.register(programa_Formacion)

