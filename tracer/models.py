from django.db import models

# Create your models here.

class Doc(models.Model):
    upload = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)

class Doc2(models.Model):
    upload = models.ImageField(upload_to='videos/')

    def __str__(self):
        return str(self.pk)