from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class SubArea(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)



class Address(models.Model):
    sub_area = models.ForeignKey(SubArea, on_delete=models.CASCADE)

class Cafe(models.Model):
    name = models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    subarea = models.ForeignKey(Address, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)