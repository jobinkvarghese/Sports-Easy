from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.index),
     path('code', views.code),
     path('userhome', views.userhome,),
     path('userlogin', views.userlogin),
     path('userreg', views.userreg),
     path('header', views.header),
     path('footer', views.footer),
     path('turf_view', views.turf_view),
     path('event_view', views.event_view),
     path('academy_view', views.academy_view),
     path('product_list', views.product_list),
     path('cart', views.cart,),
     path('product_details',views.product_details),
 
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
