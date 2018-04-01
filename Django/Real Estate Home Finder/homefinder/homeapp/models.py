from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_type = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name


class Property(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    floors = models.CharField(max_length=200)
    bedrooms = models.CharField(max_length=200)
    bathrooms = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    photo1 = models.CharField(max_length=500, null=True, blank=True)
    photo2 = models.CharField(max_length=500, null=True, blank=True)
    photo3 = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.property_name
