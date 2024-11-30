from django.contrib import admin
from . models import ChatModel
# Register your models here.

@admin.register(ChatModel)
class AdminChatModel(admin.ModelAdmin):
    list_display = [
        'sender',
        'message',
        'thread_name',
        'timestamp'
    ]