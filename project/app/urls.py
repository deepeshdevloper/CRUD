from django.urls import path,include

from .views import *
urlpatterns = [
    path("",RegisterPage,name="registerpage"),
    path("register/",UserRegister,name="register"),
    path("loginpage/",LoginPage,name="loginpage"),
    path("loginuser/",LoginUser,name="login"),

    path("queryinsert/",queryinsert,name="queryinsert"),
    path("queryshow/<str:pk>",queryshow,name="queryshow"),
    path('delete/<int:pk>',delete,name='delete'),
    path('edit/<int:pk>',edit,name='edit'),
    path('update/<int:pk>',update,name='update')
]