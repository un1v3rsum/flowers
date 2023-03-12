from rest_framework import serializers
from .models import Flower

#flowerserializer class in other words converts python object --> json
class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id','sepal_length','sepal_ratio','sepal_width','petal_length','petal_ratio','petal_width','species']
