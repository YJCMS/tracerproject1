from django.db import models

# 장고 모델

class Doc(models.Model):
    upload = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)

class Doc2(models.Model):
    upload = models.ImageField(upload_to='videos/')

    def __str__(self):
        return str(self.pk)