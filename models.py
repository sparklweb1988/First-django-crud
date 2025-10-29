from django.db import models

# Create your models here.
class Info(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    age  = models.IntegerField()
    
    def __str__(self):
        return self.full_name