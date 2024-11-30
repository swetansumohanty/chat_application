from django.contrib import admin
from . models import ChatUser
# Register your models here.
@admin.register(ChatUser)
class AdminChatUser(admin.ModelAdmin):
    list_display = ['id','username','email','mobile','password']