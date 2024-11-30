from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from . models import ChatModel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/index1.html', context={'users': users})

@csrf_exempt
def chatPage(request, username):
    try:
        login_user = User.objects.get(username=request.user)
        other_user = User.objects.get(username=username)
        if login_user.id > other_user.id:
            thread_name = f'chat_{login_user.id}-{other_user.id}'
        else:
            thread_name = f'chat_{other_user.id}-{login_user.id}'

        message_objs = ChatModel.objects.filter(thread_name=thread_name)

        context = {
            'l_user':other_user.id,
            'n_user':str(request.user),
            'messages': message_objs
        }
        return render(request, 'chat/chat.html',context)

    except Exception as e:
        return HttpResponse('OOPs, something went wrong..!')

