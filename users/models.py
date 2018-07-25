
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
