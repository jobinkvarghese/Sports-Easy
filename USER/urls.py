from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.index),
     path('userhome', views.userhome,),
     path('userlogin', views.userlogin),
     path('userreg', views.userreg),
     path('header', views.header),
     path('footer', views.footer),
     path('sports_items/', views.sports_items),
     path('turf_view', views.turf_view),
     path('event_view', views.event_view),
     path('academy_view', views.academy_view),
     path('view', views.view,),
 
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
