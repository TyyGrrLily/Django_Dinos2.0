from django.contrib import admin

# Register your models here.

from catalog.models import Animal, Environment

#admin.site.register(Animal)
#admin.site.register(Environment)

class EnvironmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Environment, EnvironmentAdmin)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('species', 'environment')