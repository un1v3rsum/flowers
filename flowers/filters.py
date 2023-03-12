import django_filters
from .models import Flower

#defining filter class
class FlowerFilter(django_filters.FilterSet):

    class Meta:
        model = Flower
        fields = ['sepal_length','sepal_ratio','sepal_width','petal_length','petal_ratio','petal_width','species']



