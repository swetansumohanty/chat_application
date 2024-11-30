from sqlite3 import Timestamp
from django.db import models
from a_user.models import ChatUser

# Create your models here.

class Chat(models.Model):
    """
    stores messages of the client in Chat table.
    """ 
   
    content = models.CharField(max_length=200)
    Timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE)
    c_user = models.CharField(max_length=30,default=None)


class Group(models.Model):
    """
    stores group created by the user in Group table.
    """
    name = models.CharField(max_length=30)

    # display group name in the admin interface
    def __str__(self):
        return self.name