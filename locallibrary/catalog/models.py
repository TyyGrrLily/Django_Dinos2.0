from django.db import models
#from django.urls import reverse

# Create your models here.
'''class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    #Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

    #Metadata
    class Meta:
        ordering =['-my_field_name']

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("model-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

class Animals(models.Model):
    """Model representing creatures."""
    name = models.CharField(max_length=200, help_text='Enter a creatures name')
    description = models.TextField(max_length=10000)

    def _str_(self):
        """String for representing the Model object."""
        return self.name
'''
class Environment(models.Model):
    
    name = models.CharField(max_length=200, help_text='Enter a environment (e.g. Dessert)')
    
    def __str__(self):
        
        return self.name

#from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Animal(models.Model):
    
    species = models.CharField(max_length=200, default='unknown')

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    #author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    #about = models.TextField(max_length=1000, help_text='Enter a brief description of the animal')
    #isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    environment = models.ForeignKey(Environment, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.species
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('animal-detail', args=[str(self.id)])
    