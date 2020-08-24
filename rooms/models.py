# import os #python
from django.db import models  # django
from core import models as core_models  # thirdparty addps
from django_countries.fields import CountryField  # my packages
from users import models as user_models
# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """Abstract model """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name_plural = "Room Types"
        # ordering = ['created']
        ordering = ['name']


class Amenity(AbstractItem):
    """ roomType model Definition """
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility model Definition """
    class Meta:

        verbose_name_plural = "Facilities"


class Houserule(AbstractItem):
    """ Facility model Definition """
    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """


# create , update field
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instantbook = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE)  # find user with ID #if user deleted, his rooms also deleted
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(Houserule, blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
