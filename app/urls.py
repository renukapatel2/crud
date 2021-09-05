from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Cruds,name="cruds"),
    path("register/",views.register,name="registeruser"),
    path("add/",views.adduser,name="add"),
    path("udelete/<int:pk>",views.UserDelete,name="udelete"),
    path("edituser/<int:pk>/",views.Edituser,name="edituser"),
    path('updat-/<int:pk>/',views.Update,name='upd')
    
]    
