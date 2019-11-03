from django.contrib import admin

# Register your models here.

from catalog.models import Animal, Environment

admin.site.register(Animal)
admin.site.register(Environment)