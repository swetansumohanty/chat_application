from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from . models import ChatUser
from . forms import SignUpForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def log_in(request):
    """
    Login a user.
    """
    try:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST,)
            nm = fm.request.POST.get('username')
            pa = fm.request.POST.get('password')
            try:
                user = ChatUser.objects.get(username=nm,password=pa)
                if user is not None:
                    login(request,user)
                    
                    return redirect('/u_profile/')
            except Exception as e:
                messages.error(request,'Bad Credentials')
        else:
            fm = AuthenticationForm()
        
        return render(request,'a_user/login.html',{'form':fm})

    except Exception as e:
        return HttpResponse('OOPs, something went wrong ..!')
        
def sign_up(request):
    """
    create new user.
    """
    try:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                nm = request.POST['username']
                fn = request.POST['first_name']
                ln = request.POST['last_name']
                em = request.POST['email']
                mo = request.POST['mobile']
                pa = request.POST['password']
                reg = ChatUser(
                    username = nm,
                    first_name = fn,
                    last_name = ln,
                    email = em,
                    mobile = mo,
                    password = pa
                )
                if ChatUser.objects.filter(username=nm):
                    
                    messages.error(request,'username already exists try new')

                elif ChatUser.objects.filter(email=em):

                    messages.error(request,'email already exists')

                elif ChatUser.objects.filter(mobile=mo):

                    messages.error(request,'mobile number already exists')

                else:
                    reg.save()
                    messages.success(request,'You are Registered Successfully , login Now !!')
                    return redirect('/')
                
        else:
            fm = SignUpForm()
        return render(request,'a_user/signup.html',{'form':fm})

    except Exception as e:
        return HttpResponse('OOPs, something went wrong ..!')
        



def profile(request):
    """
    profile description.
    """
    try:
        if request.user.is_authenticated:

            return render(request,'a_user/profile.html',{'name':request.user})
        else:

            return redirect('/')
    except Exception as e:

        return HttpResponse('OOPs, something went wrong ..!')

def log_out(request):
    """
    log out a user from his/her account.
    """
    logout(request)
    return redirect('/')