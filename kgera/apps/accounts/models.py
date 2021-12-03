from django.db import models
from django.contrib.auth.models import AbstractUser

from ..structure.models import Houses
# Create your models here.

ADMIN = 1
SEC = 2
BASIC = 3

USERTYPE_CHOICES = (
    (ADMIN, 'Administrator'),
    (SEC, 'Secretary'),
    (BASIC, 'Basic User'),
)


class User(AbstractUser):
    # User type
    user_type = models.PositiveSmallIntegerField(choices=USERTYPE_CHOICES, default=SEC)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'user_type']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.ForeignKey(Houses, on_delete=models.DO_NOTHING, to_field='housecode', null=True)
    image = models.ImageField(default='default_prof1.png', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
