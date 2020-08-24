from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# it is just data


class User(AbstractUser):
    """costum User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    ENGLISH = "en"
    KOREAN = "kr"

    CURRENCY_USD = "usd"
    CURRENCY_KR = "kw"

    GENDER_CHOICES = (
        (GENDER_MALE, "MALE"),
        (GENDER_FEMALE, "FEMALE"),
        (GENDER_OTHER, "OTHER"),
    )

    LANGUAGE_CHOICES = (
        (ENGLISH, "En"),
        (KOREAN, "Kr"),

    )

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KR, "KR")

    )

    avatar = models.ImageField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
