from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blogapp-home'),
    path('about/', views.about, name='blogapp-about'),
]
