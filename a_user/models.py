from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChatUser(User):
    """
    This class stores data of user,
    such as username,first_name etc.
    """
    mobile = models.IntegerField()
