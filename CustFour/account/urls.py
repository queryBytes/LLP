from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home-page"),
    path('register', views.register, name="registration"),
    path('login', views.login, name="login-page"),
    path('welcome', views.welcome, name="welcome"),
]