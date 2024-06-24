from .views import *
from django.urls import path
from django.shortcuts import render




urlpatterns = [
    path('list', car_list_view, name='list'),
    path('list/<int:pk>', car_detail_view, name='detail'),
    path('showroom', showroom_list_view.as_view(), name='showroomView'),    
    path('showroom/<int:pk>', showroom_details.as_view(), name='showroomDetails'),

]


