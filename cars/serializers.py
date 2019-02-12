from cars.models import Car
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    plate_num = serializers.CharField(max_length=6, required=True)
    owner = serializers.CharField(max_length=100, required=True)
    model = serializers.CharField(max_length=100, required=True)
    class Meta:
        model = Car
        fields = ('url', 'plate_num', 'owner', 'model')

