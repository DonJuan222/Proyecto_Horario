from django.contrib import admin

from .models import centro_Formacion
from .models import programa_Formacion
from .models import tipo_Instructor
from .models import trimestre_uno
from .models import trimestre_dos
from .models import trimestre_tres
from .models import trimestre_cuatro


# Register your models here.

admin.site.register(centro_Formacion)
admin.site.register(programa_Formacion)
admin.site.register(tipo_Instructor)
admin.site.register(trimestre_uno)
admin.site.register(trimestre_dos)
admin.site.register(trimestre_tres)
admin.site.register(trimestre_cuatro)