from django.db import models

# Create your models here.
class Trainee(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField(default=21)
    email=models.EmailField()
    img=models.CharField(max_length=100,null=True)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

    def __str__(self):
        return  'Name:'+self.name+' email:'+self.email