from django. contrib.auth.models import User
from django.db import models

# Create your models here.
class Jersey(models.Model): #Jersey extends(inherites) from the models.Model class (has name, decription and slug) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)