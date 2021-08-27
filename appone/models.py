from django.db import models

# Create your models here.

class datac(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=(100))