from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage for password generator
    path('password/', views.password, name='password'),  # Page to show generated password
]
