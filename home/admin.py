from django.contrib import admin

from .models import municipio
from .models import ambiente
from .models import horario
from .models import instructor

# Register your models here.



admin.site.register(municipio)
admin.site.register(ambiente)
admin.site.register(horario)
admin.site.register(instructor)

