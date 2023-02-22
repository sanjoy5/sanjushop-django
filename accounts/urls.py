from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registerPage,name='register'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('',dashboard,name='dashboard'),

    path('activate/<uidb64>/<token>/',activate,name='activate'),
    path('forgot_password',forgotPassword,name='forgot_password'),

    path('reset_password_validate/<uidb64>/<token>/',reset_password_validate,name='reset_password_validate'),
    path('reset_password/',resetPassword,name='reset_password'),
]
