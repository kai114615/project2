from django.urls import path
from home import views


urlpatterns = [
    path('', views.index),
    path('country/', views.country),
    path('categories/', views.categories),
    path('cities/', views.cities)
]