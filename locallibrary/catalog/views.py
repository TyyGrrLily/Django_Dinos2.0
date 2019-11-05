from django.shortcuts import render

# Create your views here.
from catalog.models import Animal, Environment

def index(request):
   """View function for home page of siye."""
   num_animals = Animal.objects.all().count()
   num_envirnoments = Environment.objects.count()

   context = {
       'num_animals': num_animals,
       'num_envirnoments': num_envirnoments,
   }

   return render(request, 'index.html', context=context)