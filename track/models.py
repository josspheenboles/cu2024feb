from django.db import models

# Create your models here.
class Track(models.Model):
    name=models.CharField(max_length=10)
    @classmethod
    def get_all_tracks(cls):
        return [(obj.id,obj.name) for obj in cls.objects.all()]
    def __str__(self):
        return self.name