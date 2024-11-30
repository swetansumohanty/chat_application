from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

# Create your views here.

def index(request,gname):
    """
    checks if group present in the db or creates one if not.
    """
    try:
        if request.user.is_authenticated:
            group = models.Group.objects.filter(name=gname).first()
            chats=[]
            if group:
                chats = models.Chat.objects.filter(group=group)
            else:
                group = models.Group(name=gname)
                group.save()

            return render(request,'app/index.html',{"groupname":gname,'chats':chats,'user':request.user})
        else:
            return redirect('/')
    except Exception as e:
        return HttpResponse('OOPs, something went wrong..!')