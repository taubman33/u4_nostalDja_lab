from django.contrib import admin

# Register your models here.
from .models import Decade
from .models import Fad

admin.site.register(Decade)
admin.site.register(Fad)