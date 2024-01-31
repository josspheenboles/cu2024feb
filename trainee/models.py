from django.db import models

# Create your models here.
class Trainee(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField(default=21)
    email=models.EmailField()
    img=models.CharField(max_length=100)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)