from rest_framework import serializers
class Traineeserlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    img=serializers.ImageField()
    createdat=serializers.DateTimeField(read_only=True)
