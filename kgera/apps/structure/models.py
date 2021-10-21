from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.forms.widgets import Widget
from django.utils.translation import deactivate

# Create your models here.
NONE = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10

COUNT_CHOICES = (
    (NONE, ('None')),
    (ONE, ('One')),
    (TWO, ('Two')),
    (THREE, ('Three')),
    (FOUR, ('Four')),
    (FIVE, ('Five')),
    (SIX, ('Six')),
    (SEVEN, ('Seven')),
    (EIGHT, ('Eight')),
    (NINE, ('Nine')),
    (TEN, ('Ten')),
)


class HouseType(models.Model):
      
    htype = models.CharField('House Type', unique= True, max_length=200)
    is_block = models.BooleanField(default=False)
    block_count = models.PositiveSmallIntegerField(choices=COUNT_CHOICES, default=ONE)
    is_flat = models.BooleanField(default=False)
    flat_count = models.PositiveSmallIntegerField(choices=COUNT_CHOICES, default=ONE)

    def __str__(self):
        return f"{self.htype}"

class CommunityType(models.Model):
    housetype = models.OneToOneField(HouseType, on_delete=models.CASCADE)
    commtype = models.CharField('Community Type Code', max_length=3, default='A')
    description = models.TextField(default="Description of the Community Type")


    def __str__(self):
        return f"{self.commtype}"


class Community(models.Model):
    communitytype = models.ForeignKey(CommunityType, on_delete=CASCADE)
    commnum = models.IntegerField(default=1)
    commcode = models.CharField('Community Code', max_length=5, unique=True)

    def __str__(self):
        return f"{self.commcode}"

class Houses(models.Model):
    VACANT = 0
    OCCUPIED = 1

    STATUS = (
        (VACANT, ('Vacant')),
        (OCCUPIED, ('Occupied'))
    )

    community = models.ForeignKey(Community, on_delete= CASCADE)
    housecode = models.CharField(unique=True, max_length=200)
    housestatus = models.PositiveSmallIntegerField(choices=STATUS, default=VACANT)
    
    def __str__(self):
        return f"{self.housecode}"


