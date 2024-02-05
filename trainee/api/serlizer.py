from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from trainee.models import *
class Traineeserlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[UniqueValidator(queryset=Trainee.objects.all())],max_length=50)
    img=serializers.ImageField(allow_empty_file=True)
    createdat=serializers.DateTimeField(read_only=True)

