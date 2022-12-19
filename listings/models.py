from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    name=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(max_length=50)
    biography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2021)]
    )
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True,blank=True)

    class Genre(models.TextChoices):
        HIP_HOP='HH'
        SYNTH_POP='SP'
        ALTERNATIVE_ROCH='AR'
    genre=models.fields.CharField(choices=Genre.choices,max_length=5)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=1000)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(
        null=True,
        validators=[MinValueValidator(1900),MaxValueValidator(2021)]
    )
    class ListingType(models.TextChoices):
        RECORDS='R'
        CLOTHING='C'
        POSTERS='P'
        Misc='M'
    type=models.fields.CharField(choices=ListingType.choices,max_length=5)

    band=models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)




# Create your models here.
