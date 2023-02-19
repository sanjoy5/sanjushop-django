from django.urls import path
from .views import *

urlpatterns = [
    path('register',registerPage,name='register'),
    path('login',loginPage,name='login'),
    path('logout',logoutPage,name='logout'),
]
