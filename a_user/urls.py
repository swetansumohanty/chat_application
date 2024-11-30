from django.urls import path
from . import views

# define your routes here

urlpatterns = [
    path('',views.log_in,name='login'),
    path('sign_up/',views.sign_up,name='signup'),
    path('u_profile/',views.profile,name='prfile'),
    path('u_logout/',views.log_out,name='logout')
]
