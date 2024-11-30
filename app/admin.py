from django.contrib import admin
from . models import Chat,Group

# Register your models here.

@admin.register(Chat)
class AdminChat(admin.ModelAdmin):
    """
    provides an interface for Chat model with attributes
    """
    list_display = ['id','content','Timestamp','group','c_user']


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    """
    provides an interface for Group model with attributes
    """
    list_display = ['id','name']