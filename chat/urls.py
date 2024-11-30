from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('<str:username>/',views.chatPage,name='p_chat')
]
