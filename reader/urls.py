from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.ReaderSignup.as_view()),
    path('login', views.Login.as_view()),
    
]