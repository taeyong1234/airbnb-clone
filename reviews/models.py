from django.db import models
from core import models as core_models
# Create your models here.


class Review(core_models.TimeStampedModel):

    """Review Model Dfinition"""
    review = models.TextField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    communication = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"