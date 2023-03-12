from django.db import models

#defining Flower class and its attributes
class Flower(models.Model):
    sepal_length = models.FloatField(max_length=3)
    sepal_ratio = models.FloatField(max_length=3)
    sepal_width = models.FloatField(max_length=3)
    petal_length = models.FloatField(max_length=3)
    petal_ratio = models.FloatField(max_length=3)
    petal_width = models.FloatField(max_length=3)
    species = models.CharField(max_length=100)



