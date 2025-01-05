from django.db import models

# Create your models here.


class Categories(models.Model):
    catName = models.CharField(max_length=100)
    catSpec = models.CharField(max_length=250)


