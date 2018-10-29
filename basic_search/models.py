from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Favourite(models.Model):
    user = models.ForeignKey(User)
    fav = models.URLField(max_length=1000)