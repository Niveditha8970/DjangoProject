from django.urls import path
from wolfapp import views

urlpatterns = [
    
    path('about',views.about),
    path('classes',views.classes),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('abc',views.abc),
    path('math',views.math),
    path('base',views.reuse),
    path('contact',views.contact),
    path('',views.index),
    path('dash',views.dashboard),
    path('create_post',views.create_post),
    path('catfilter/<value>',views.catfilter),
    path('actfilter/<value>',views.actfilter),
    path('dform',views.djangoform),
    path('dmodelform',views.djangomodelform),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('setcookies',views.setcookies),
    path('getcookies',views.getcookies),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
   

]