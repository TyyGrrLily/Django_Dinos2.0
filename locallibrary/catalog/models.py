from django.db import models
from django.urls import reverse

# Create your models here.
class MyModelName(models.Model):
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
    name = models.CharField(max_length=20, help_text='Enter a creatures name')
    description = models.TextField(max_length=10000)

    def _str_(self):
        """String for representing the Model object."""
        return self.name
