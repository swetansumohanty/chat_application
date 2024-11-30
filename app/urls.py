from django.urls import path
from . import views

#urlpatterns

urlpatterns = [
    path('chat/<str:gname>/',views.index,name='index')
]
