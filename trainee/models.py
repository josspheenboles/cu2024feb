from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Trainee(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField(default=21)
    email=models.EmailField()
    img=models.ImageField(upload_to='trainee/images',blank=True,null=True)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

    def __str__(self):
        return  'Name:'+self.name+' email:'+self.email

    @classmethod
    def get_all_trainees(cls):
        return cls.objects.all()

    @classmethod
    def get_trainee_by_id(self,id):
        return self.objects.get(id=id)

    def get_trainee_url(self,id):
        return reverse('trainee.details',args=[id])

    @classmethod
    def get_trainee_img(self,id):
        return 'media'+self.objects.get(id=id).img
