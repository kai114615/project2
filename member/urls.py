from django.urls import path
from member import views

urlpatterns = [
    path('', views.index),
    path('mobile/', views.mobile),
    path('register/', views.register)
]