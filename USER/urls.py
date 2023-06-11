from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index),
     path('userhome', views.userhome,),
     path('userlogin', views.userlogin),
     path('userreg', views.userreg),
     path('header', views.header),
     path('footer', views.footer),
     path('sports_items', views.sports_items),
     path('turf_view', views.turf_view),
     path('event_view', views.event_view),
     path('academy_view', views.academy_view),
 
 
]
