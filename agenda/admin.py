from django.contrib import admin
from .models import agenda
from .models import dias
from .models import integracion

# # Register your models here.
admin.site.register(agenda)
admin.site.register(dias)
admin.site.register(integracion)



