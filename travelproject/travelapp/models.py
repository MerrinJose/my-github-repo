from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='galllery')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Chefs(models.Model):
    Cname = models.CharField(max_length=250)
    Cimg = models.ImageField(upload_to='galllery')
    Cdesc = models.TextField()

    def __str__(self):
        return self.Cname
