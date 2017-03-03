from django.contrib import admin
from .models import *

admin.site.register(Album)
admin.site.register(Song)

#for å gjøre questions tilgjengelig på admin.
admin.site.register(Question)