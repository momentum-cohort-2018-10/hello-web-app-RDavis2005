from django.db import models

# Create your models here.
class Thing(models.Model): #Dog extends(inherites) from the models.Model class (has name, decription and slug) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)