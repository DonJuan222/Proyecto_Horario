from django.contrib import admin

from .models import *


# Register your models here.

admin.site.register(municipio)
admin.site.register(ambiente)
admin.site.register(sede)
admin.site.register(tipoInstructor)
admin.site.register(tipoPrograma)
admin.site.register(instructor)

