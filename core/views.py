from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @csrf_exempt
def home(request):
    try:

        if request.method == 'POST':
            name = request.POST.get('name')
            user = request.user
            return HttpResponseRedirect(f'/chat/{name}/?user={user}')

        else:
            pass
        return render(request,'core/core.html')

    except Exception as e:
        return HttpResponse('OOPs, something went wrong..!')
        