from django.db import models

# Create your models here.

class Home(models.Model):
    username = models.CharField(max_length=222)
    email = models.EmailField()
    password = models.CharField(max_length=222)
    phone = models.CharField(max_length=222)


    def __str__(self):
        return self.username