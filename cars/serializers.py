from rest_framework import serializers
from .models import *

class CarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user', 'brand')





class CarDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'