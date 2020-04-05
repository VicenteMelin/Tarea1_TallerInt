from django.db import models


class Episode(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    air_date = models.CharField(max_length=200)
    episode = models.CharField(max_length=200)
    characters = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    episode = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    dimension = models.CharField(max_length=200)
    residents = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

    def __str__(self):
        return self.name
