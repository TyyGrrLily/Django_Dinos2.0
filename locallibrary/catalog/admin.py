from django.contrib import admin

# Register your models here.

from catalog.models import Animals, Environment

admin.site.register(Animals)
admin.site.register(Environment)